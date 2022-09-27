import React, { useState } from 'react'

export const App = () => {
  const [value, setValue] = useState(0)

  const increment = () => {
    setValue(value + 1)
  }

  const decrement = () => {
    setValue(value - 1)
  }

  return (
    <>
      <h1>Simple Counter App</h1>
      <div>
        <button onClick={decrement} style={{marginRight: 10}} > - </button>
        <span>{value}</span>
        <button onClick={increment} style={{marginLeft: 10}}> + </button>
      </div>
    </>
  )
}
