function see(event)
{ event.preventDefault()
  let t = document.getElementById('password').type
  console.log(t)
  if(t == 'password')
  {
    document.getElementById('password').type = 'text'
  }
  else
  {
    document.getElementById('password').type = 'password'
  }
}
