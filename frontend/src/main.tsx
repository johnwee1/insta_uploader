import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import Form from './Form.tsx'
import ServerStatus from './ServerStatus.tsx'
import './index.css'

createRoot(document.getElementById('root')!).render(
  <div style={{ display: 'flex', flexDirection: 'column', height: '100vh' }}>
    <StrictMode>
      <Form />
      <ServerStatus />
    </StrictMode>
  </div>,
)
