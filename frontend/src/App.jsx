import { useState } from 'react'
import axios from 'axios'
import './App.css'
import graphImages from './graphs.json'

function App() {
  const [formData, setFormData] = useState({
    market_id: 1.0,
    store_primary_category: 'american',
    order_protocol: 1.0,
    total_items: 2,
    subtotal: 1500,
    num_distinct_items: 2,
    min_item_price: 500,
    max_item_price: 1000,
    total_outstanding_orders: 10,
    estimated_store_to_consumer_driving_duration: 400,
    created_at: new Date().toISOString()
  })

  const [prediction, setPrediction] = useState(null)
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState(null)
  const [showGraphs, setShowGraphs] = useState(false)

  const handleChange = (e) => {
    const { name, value } = e.target
    setFormData(prev => ({
      ...prev,
      [name]: value
    }))
  }

  const handleSubmit = async (e) => {
    e.preventDefault()
    setLoading(true)
    setError(null)
    setPrediction(null)

    try {
      const payload = {
        ...formData,
        market_id: parseFloat(formData.market_id),
        order_protocol: parseFloat(formData.order_protocol),
        total_items: parseInt(formData.total_items),
        subtotal: parseInt(formData.subtotal),
        num_distinct_items: parseInt(formData.num_distinct_items),
        min_item_price: parseInt(formData.min_item_price),
        max_item_price: parseInt(formData.max_item_price),
        total_outstanding_orders: parseFloat(formData.total_outstanding_orders),
        estimated_store_to_consumer_driving_duration: parseFloat(formData.estimated_store_to_consumer_driving_duration),
        created_at: new Date().toISOString()
      }

      const response = await axios.post('http://localhost:8000/predict', payload)
      setPrediction(response.data.predicted_delivery_time_minutes)
    } catch (err) {
      console.error(err)
      setError('Failed to get prediction. Ensure backend is running.')
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="container">
      <header className="header">
        <h1 className="title">Porter Delivery AI</h1>
        <p className="subtitle">Neural Network Powered Delivery Time Estimation</p>
        <button className="graph-btn" onClick={() => setShowGraphs(!showGraphs)}>
          {showGraphs ? 'Hide Analysis' : 'View Case Study Graphs'}
        </button>
      </header>

      {showGraphs ? (
        <div className="graph-gallery">
          {console.log('Graph images:', graphImages)}
          {graphImages && graphImages.length > 0 ? (
            graphImages.map((item) => (
              <div key={item.id} className="graph-card">
                <div className="graph-image-container">
                  <img
                    src={`/${item.src}`}
                    alt={`Analysis from ${item.source_pdf}`}
                    onLoad={() => console.log(`Loaded: ${item.src}`)}
                    onError={(e) => {
                      console.error(`Failed to load: ${item.src}`)
                      e.target.style.border = '2px solid red'
                    }}
                  />
                </div>
                <div className="graph-content">
                  <p className="graph-source">Source: {item.source_pdf} (Page {item.page})</p>
                  <p className="graph-text">{item.context}</p>
                </div>
              </div>
            ))
          ) : (
            <div style={{ color: 'white' }}>No graphs found. Check console for errors.</div>
          )}
        </div>
      ) : (
        <div className="main-card">
          <form onSubmit={handleSubmit}>
            <div className="form-grid">
              <div className="form-group">
                <label className="label">Market ID</label>
                <input type="number" name="market_id" value={formData.market_id} onChange={handleChange} className="input" required />
              </div>

              <div className="form-group">
                <label className="label">Store Category</label>
                <select
                  name="store_primary_category"
                  value={formData.store_primary_category}
                  onChange={handleChange}
                  className="input"
                  required
                >
                  <option value="american">American</option>
                  <option value="italian">Italian</option>
                  <option value="chinese">Chinese</option>
                  <option value="indian">Indian</option>
                  <option value="mexican">Mexican</option>
                  <option value="japanese">Japanese</option>
                  <option value="thai">Thai</option>
                  <option value="mediterranean">Mediterranean</option>
                  <option value="pizza">Pizza</option>
                  <option value="burger">Burger</option>
                  <option value="sandwich">Sandwich</option>
                  <option value="dessert">Dessert</option>
                  <option value="coffee">Coffee</option>
                  <option value="healthy">Healthy</option>
                  <option value="vegan">Vegan</option>
                  <option value="seafood">Seafood</option>
                  <option value="bbq">BBQ</option>
                  <option value="fast_food">Fast Food</option>
                </select>
              </div>

              <div className="form-group">
                <label className="label">Order Protocol</label>
                <input type="number" name="order_protocol" value={formData.order_protocol} onChange={handleChange} className="input" required />
              </div>

              <div className="form-group">
                <label className="label">Total Items</label>
                <input type="number" name="total_items" value={formData.total_items} onChange={handleChange} className="input" required />
              </div>

              <div className="form-group">
                <label className="label">Subtotal (cents)</label>
                <input type="number" name="subtotal" value={formData.subtotal} onChange={handleChange} className="input" required />
              </div>

              <div className="form-group">
                <label className="label">Distinct Items</label>
                <input type="number" name="num_distinct_items" value={formData.num_distinct_items} onChange={handleChange} className="input" required />
              </div>

              <div className="form-group">
                <label className="label">Min Item Price</label>
                <input type="number" name="min_item_price" value={formData.min_item_price} onChange={handleChange} className="input" required />
              </div>

              <div className="form-group">
                <label className="label">Max Item Price</label>
                <input type="number" name="max_item_price" value={formData.max_item_price} onChange={handleChange} className="input" required />
              </div>

              <div className="form-group">
                <label className="label">Outstanding Orders</label>
                <input type="number" name="total_outstanding_orders" value={formData.total_outstanding_orders} onChange={handleChange} className="input" required />
              </div>

              <div className="form-group">
                <label className="label">Est. Driving Duration (sec)</label>
                <input type="number" name="estimated_store_to_consumer_driving_duration" value={formData.estimated_store_to_consumer_driving_duration} onChange={handleChange} className="input" required />
              </div>
            </div>

            <button type="submit" className="submit-btn" disabled={loading}>
              {loading ? 'Calculating...' : 'Predict Delivery Time'}
            </button>
          </form>

          {error && <div style={{ color: '#ef4444', marginTop: '1rem', textAlign: 'center' }}>{error}</div>}

          {prediction !== null && (
            <div className="result-section">
              <div className="result-label">Estimated Delivery Time</div>
              <div className="result-value">
                {prediction}
                <span className="result-unit">min</span>
              </div>
            </div>
          )}
        </div>
      )}
    </div>
  )
}

export default App
