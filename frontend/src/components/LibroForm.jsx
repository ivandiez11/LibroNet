import { useState, useEffect } from 'react'
import { createLibro, updateLibro } from '../services/api'
import '../styles/LibroForm.css'

function LibroForm({ libro, onSuccess, onCancel }) {
  const [formData, setFormData] = useState({
    titulo: '',
    autor: '',
    editorial: '',
    isbn: '',
    anio_publicacion: '',
    categoria: '',
    ejemplares: 1,
    disponible: 1,
  })
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState(null)

  useEffect(() => {
    if (libro) {
      setFormData({
        titulo: libro.titulo || '',
        autor: libro.autor || '',
        editorial: libro.editorial || '',
        isbn: libro.isbn || '',
        anio_publicacion: libro.anio_publicacion || '',
        categoria: libro.categoria || '',
        ejemplares: libro.ejemplares || 1,
        disponible: libro.disponible || 1,
      })
    }
  }, [libro])

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

    try {
      // Convertir valores numéricos
      const data = {
        ...formData,
        ejemplares: parseInt(formData.ejemplares) || 1,
        disponible: parseInt(formData.disponible) || 1,
        anio_publicacion: formData.anio_publicacion ? parseInt(formData.anio_publicacion) : null,
      }

      // Eliminar campos vacíos opcionales
      if (!data.editorial) delete data.editorial
      if (!data.isbn) delete data.isbn
      if (!data.categoria) delete data.categoria

      if (libro) {
        await updateLibro(libro.id_libro, data)
      } else {
        await createLibro(data)
      }

      onSuccess()
    } catch (err) {
      setError(err.response?.data?.detail || 'Error al guardar el libro')
      console.error('Error:', err)
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="form-container">
      <h2>{libro ? 'Editar Libro' : 'Nuevo Libro'}</h2>
      
      {error && (
        <div className="error-message">
          {error}
        </div>
      )}

      <form onSubmit={handleSubmit} className="libro-form">
        <div className="form-row">
          <div className="form-group">
            <label htmlFor="titulo">Título *</label>
            <input
              type="text"
              id="titulo"
              name="titulo"
              value={formData.titulo}
              onChange={handleChange}
              required
              maxLength={255}
            />
          </div>

          <div className="form-group">
            <label htmlFor="autor">Autor *</label>
            <input
              type="text"
              id="autor"
              name="autor"
              value={formData.autor}
              onChange={handleChange}
              required
              maxLength={255}
            />
          </div>
        </div>

        <div className="form-row">
          <div className="form-group">
            <label htmlFor="editorial">Editorial</label>
            <input
              type="text"
              id="editorial"
              name="editorial"
              value={formData.editorial}
              onChange={handleChange}
              maxLength={255}
            />
          </div>

          <div className="form-group">
            <label htmlFor="isbn">ISBN</label>
            <input
              type="text"
              id="isbn"
              name="isbn"
              value={formData.isbn}
              onChange={handleChange}
              maxLength={20}
            />
          </div>
        </div>

        <div className="form-row">
          <div className="form-group">
            <label htmlFor="anio_publicacion">Año de Publicación</label>
            <input
              type="number"
              id="anio_publicacion"
              name="anio_publicacion"
              value={formData.anio_publicacion}
              onChange={handleChange}
              min={1000}
              max={9999}
            />
          </div>

          <div className="form-group">
            <label htmlFor="categoria">Categoría</label>
            <input
              type="text"
              id="categoria"
              name="categoria"
              value={formData.categoria}
              onChange={handleChange}
              maxLength={100}
              placeholder="Ej: Ficción, Ciencia, Historia..."
            />
          </div>
        </div>

        <div className="form-row">
          <div className="form-group">
            <label htmlFor="ejemplares">Ejemplares Totales *</label>
            <input
              type="number"
              id="ejemplares"
              name="ejemplares"
              value={formData.ejemplares}
              onChange={handleChange}
              required
              min={0}
            />
          </div>

          <div className="form-group">
            <label htmlFor="disponible">Ejemplares Disponibles *</label>
            <input
              type="number"
              id="disponible"
              name="disponible"
              value={formData.disponible}
              onChange={handleChange}
              required
              min={0}
              max={formData.ejemplares}
            />
          </div>
        </div>

        <div className="form-actions">
          <button 
            type="button" 
            className="btn btn-cancel"
            onClick={onCancel}
            disabled={loading}
          >
            Cancelar
          </button>
          <button 
            type="submit" 
            className="btn btn-primary"
            disabled={loading}
          >
            {loading ? 'Guardando...' : (libro ? 'Actualizar' : 'Crear')}
          </button>
        </div>
      </form>
    </div>
  )
}

export default LibroForm
