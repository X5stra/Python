import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import Card from './Compentes/Card'
import Hero from "./Compentes/Hero"

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
    <Hero />
    {count}
    <button onClick={() => setCount(count +1)}>+</button>
      <Card
      image="https://i.imgflip.com/1z3eja.jpg"
       name="spiderman"   
       city="brooklyn"
       job="school"
      />

      <Card
      image="https://static.wikia.nocookie.net/spidermanps4/images/c/ca/Peter_Parker_from_MSM2_headshot.png/revision/latest/scale-to-width-down/1200?cb=20240116135008"
      name="peter parker"
      city="brooklyn"
      job="spiderman"
      />

      
    </>
  )
}

export default App
