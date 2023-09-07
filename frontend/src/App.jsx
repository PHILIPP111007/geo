import "./styles/App.css"
import { useState } from "react"
import Fetch from "./API/Fetch"

const errorServer = "Error while sending to the server."

export default function App() {
	const [coordsGPS, setCoordsGPS] = useState(undefined)
	const [coordsIP, setCoordsIP] = useState(undefined)

	const [loadingGPS, setLoadingGPS] = useState(false)
	const [loadingIP, setLoadingIP] = useState(false)

	const [errorMsg, setErrorMsg] = useState("")

	const options = {
		enableHighAccuracy: true,
		maximumAge: 0,
	}

	// const watch = navigator.geolocation.watchPosition(position => {
	// 	console.log(position)
	// })

	async function createPositionGPS() {
		setLoadingGPS(true)
		setCoordsGPS(undefined)

		// https://w3c.github.io/geolocation-api/
		navigator.geolocation.getCurrentPosition(successCallback, errorCallBack, options)
	}

	async function successCallback(position) {
		setLoadingGPS(false)

		const crdsDict = {
			coords: {
				accuracy: position.coords.accuracy,
				altitude: position.coords.altitude,
				altitudeAccuracy: position.coords.altitudeAccuracy,
				heading: position.coords.heading,
				latitude: position.coords.latitude,
				longitude: position.coords.longitude,
				speed: position.coords.speed,
			},
			timestamp: position.timestamp,
		}
		setCoordsGPS(crdsDict)

		const data = await Fetch({ action: 'api/gps/', method: 'POST', body: crdsDict })
		if (data && data.ok) {
			setErrorMsg("")
			console.log('data saved.')
		} else {
			setErrorMsg(errorServer)
			console.error(errorServer)
		}
	}

	async function errorCallBack(error) {
		setLoadingGPS(false)
		setErrorMsg(error.message)
		console.error(error)
	}

	async function getPositionIP() {
		setCoordsIP(undefined)
		setLoadingIP(true)

		const data = await Fetch({ action: 'api/ip/', method: 'GET' })
		setLoadingIP(false)
		if (data && data.ok) {
			setCoordsIP(data.coords)
		}
	}

	return (
		<div className="App">
			<div className="GPS">
				<strong>See your geolocation by GPS: </strong>
				{loadingGPS
					?
					<div>Wait...</div>
					:
					<button onClick={() => createPositionGPS()}>Get</button>
				}
				<p>
					{errorMsg
						&&
						<div className="Error" onClick={() => setErrorMsg("")}>
							{errorMsg}
						</div>
					}
				</p>

				{coordsGPS
					&&
					<>
						<pre>{JSON.stringify(coordsGPS, null, 4)}</pre>
						<a
							id="map-link"
							target="_blank"
							href={`https://www.openstreetmap.org/#map=18/${coordsGPS.coords.latitude}/${coordsGPS.coords.longitude}`}
						>
							See yourself on the map
						</a>
					</>
				}
			</div>

			<div className="IP">
				<strong>See your geolocation by IP: </strong>
				{loadingIP
					?
					<div>Wait...</div>
					:
					<button onClick={() => getPositionIP()}>Get</button>
				}

				{coordsIP
					&&
					<pre>{JSON.stringify(coordsIP, null, 4)}</pre>
				}
			</div>
		</div>
	)
}