import { useState } from "react"

function App() {
  const [formData, setFormData] = useState({
    MedInc: "",
    HouseAge: "",
    AveRooms: "",
    AveBedrms: "",
    Population: "",
    AveOccup: "",
    Latitude: "",
    Longitude: ""
  })

  const handleChange = (e) => {
    const { name, value } = e.target

    setFormData({
      ...formData,
      [name]: value
    })
  }

  return (
    <div>
      <h1>House Price Prediction</h1>

      <div>
        <label>MedInc</label>
        <input
          type="number"
          name="MedInc"
          value={formData.MedInc}
          onChange={handleChange}
        />
      </div>

      <div>
        <label>House Age</label>
        <input
          type="number"
          name="HouseAge"
          value={formData.HouseAge}
          onChange={handleChange}
        />
      </div>

      <div>
        <label>Average Rooms</label>
        <input
          type="number"
          name="AveRooms"
          value={formData.AveRooms}
          onChange={handleChange}
        />
      </div>

      <div>
        <label>Average Bedrooms</label>
        <input
          type="number"
          name="AveBedrms"
          value={formData.AveBedrms}
          onChange={handleChange}
        />
      </div>

      <div>
        <label>Population</label>
        <input
          type="number"
          name="Population"
          value={formData.Population}
          onChange={handleChange}
        />
      </div>

      <div>
        <label>Average Occupancy</label>
        <input
          type="number"
          name="AveOccup"
          value={formData.AveOccup}
          onChange={handleChange}
        />
      </div>

      <div>
        <label>Latitude</label>
        <input
          type="number"
          name="Latitude"
          value={formData.Latitude}
          onChange={handleChange}
        />
      </div>

      <div>
        <label>Longitude</label>
        <input
          type="number"
          name="Longitude"
          value={formData.Longitude}
          onChange={handleChange}
        />
      </div>

      <button>Predict Price</button>
    </div>
  )
}

export default App