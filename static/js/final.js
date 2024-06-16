function rem()
{
    document.getElementById('logout').style.display = 'none'
}

function log()
{
    if(document.getElementById('logout').style.display === 'none' || document.getElementById('logout').style.display === '')
{  document.getElementById('logout').style.display = 'flex'  }
else
{  document.getElementById('logout').style.display = 'none'  }
}