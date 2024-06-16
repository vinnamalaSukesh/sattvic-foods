
var emails = document.getElementById('list').textContent
emails = emails.slice(1,emails.length-1)
emails = emails.split(',')

function validate()
  {
    let email = document.getElementById('email').value.trim().toLowerCase();
    for (let i of emails)
    {
      let cleanEmail = i.replace(/['"]+/g, '').trim().toLowerCase();
      if (cleanEmail === email)
      {
        document.getElementById('emaili').style.visibility = 'visible'
          return false
      }
    }
    document.getElementById('emaili').style.visibility = 'hidden'
    let password = document.getElementById('password').value
    console.log(password)
    if(password.length < 8)
    { console.log('password is too short')
      document.getElementById('pass').style.visibility = 'visible'
      return false;
    }
    return true;
  }

function see(event)
{ event.preventDefault()
  let t = document.getElementById('password').type
  if(t == 'password')
  {
    document.getElementById('password').type = 'text'
    console.log(document.getElementsByClassName('fa-solid fa-eye-slash'))

  }
  else
  {
    document.getElementById('password').type = 'password'
    console.log(document.getElementsByClassName('fa-solid fa-eye'))
  }
}
