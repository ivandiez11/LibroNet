import { useState } from 'react'
import { deleteLibro } from '../services/api'
import '../styles/LibrosList.css'

function LibrosList({ libros, onEdit, onDelete }) {
  const [deletingId, setDeletingId] = useState(null)

  const handleDelete = async (id) => {
    if (!window.confirm('¿Estás seguro de eliminar este libro?')) {
      return
    }

    try {
      setDeletingId(id)
      await deleteLibro(id)
      onDelete()
    } catch (error) {
      alert('Error al eliminar el libro')
      console.error('Error:', error)
    } finally {
      setDeletingId(null)
    }
  }

  if (libros.length === 0) {
    return (
      <div className="empty-state">
        <p>📚 No hay libros registrados</p>
        <p>¡Agrega tu primer libro!</p>
      </div>
    )
  }

  return (
    <div className="libros-container">
      <h2>Catálogo de Libros ({libros.length})</h2>
      <div className="libros-grid">
        {libros.map((libro) => (
          <div key={libro.id_libro} className="libro-card">
            <div className="libro-header">
              <h3>{libro.titulo}</h3>
              <span className="libro-badge">
                {libro.disponible}/{libro.ejemplares} disponibles
              </span>
            </div>
            
            <div className="libro-body">
              <p><strong>Autor:</strong> {libro.autor}</p>
              {libro.editorial && <p><strong>Editorial:</strong> {libro.editorial}</p>}
              {libro.isbn && <p><strong>ISBN:</strong> {libro.isbn}</p>}
              {libro.anio_publicacion && <p><strong>Año:</strong> {libro.anio_publicacion}</p>}
              {libro.categoria && (
                <p className="libro-categoria">
                  <span className="categoria-tag">{libro.categoria}</span>
                </p>
              )}
            </div>

            <div className="libro-actions">
              <button 
                className="btn btn-edit"
                onClick={() => onEdit(libro)}
              >
                ✏️ Editar
              </button>
              <button 
                className="btn btn-delete"
                onClick={() => handleDelete(libro.id_libro)}
                disabled={deletingId === libro.id_libro}
              >
                {deletingId === libro.id_libro ? '...' : '🗑️ Eliminar'}
              </button>
            </div>
          </div>
        ))}
      </div>
    </div>
  )
}

export default LibrosList
