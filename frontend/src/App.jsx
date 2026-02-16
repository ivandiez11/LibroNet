import { useState, useEffect } from 'react'
import './styles/App.css'
import LibrosList from './components/LibrosList'
import LibroForm from './components/LibroForm'
import { getLibros } from './services/api'

function App() {
  const [libros, setLibros] = useState([])
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState(null)
  const [editingLibro, setEditingLibro] = useState(null)
  const [showForm, setShowForm] = useState(false)

  const fetchLibros = async () => {
    try {
      setLoading(true)
      setError(null)
      const data = await getLibros()
      setLibros(data)
    } catch (err) {
      setError('Error al cargar los libros. Verifica que el backend esté ejecutándose.')
      console.error('Error:', err)
    } finally {
      setLoading(false)
    }
  }

  useEffect(() => {
    fetchLibros()
  }, [])

  const handleEdit = (libro) => {
    setEditingLibro(libro)
    setShowForm(true)
  }

  const handleCancelForm = () => {
    setEditingLibro(null)
    setShowForm(false)
  }

  const handleSuccess = () => {
    setEditingLibro(null)
    setShowForm(false)
    fetchLibros()
  }

  return (
    <div className="App">
      <header className="header">
        <h1>📚 LibroNet</h1>
        <p>Sistema de Gestión de Biblioteca</p>
      </header>

      <main className="main-content">
        <div className="controls">
          <button 
            className="btn btn-primary"
            onClick={() => setShowForm(!showForm)}
          >
            {showForm ? 'Cancelar' : '+ Agregar Libro'}
          </button>
        </div>

        {showForm && (
          <LibroForm 
            libro={editingLibro}
            onSuccess={handleSuccess}
            onCancel={handleCancelForm}
          />
        )}

        {error && (
          <div className="error-message">
            {error}
          </div>
        )}

        {loading ? (
          <div className="loading">Cargando libros...</div>
        ) : (
          <LibrosList 
            libros={libros}
            onEdit={handleEdit}
            onDelete={fetchLibros}
          />
        )}
      </main>

      <footer className="footer">
        <p>LibroNet © 2026</p>
      </footer>
    </div>
  )
}

export default App
