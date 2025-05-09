var curr_cat = 'Appetizers'
var cart_items = []
var total = 0
var itemslist = document.getElementById('itemslist').textContent
itemslist = itemslist.slice(2, itemslist.length - 2)
itemslist = itemslist.split('[')
list = []
var list_of_items = ''

for (let i of itemslist) {
  let x = i.split(',');
  let id = x[0].trim();
  let name = x[1].trim().replace(/^'/, "").replace(/'$/, "");
  let price = parseInt(x[2].trim());
  let image = x[3].trim().replace(/^'/, "").replace(/'$/, "");
  list.push([id, name, price, image]);
}

function change(changeto) {
  const newCatButton = document.getElementById(changeto + 'b');
  if (newCatButton) {
    newCatButton.style.backgroundColor = 'rgb(250, 244, 245)';
    newCatButton.style.color = 'red';
    newCatButton.style.borderColor = 'red';
    newCatButton.style.boxShadow = '0px 0px 5px red';
  }

  const newCatContent = document.getElementById(changeto);
  if (newCatContent) {
    newCatContent.style.display = 'flex';
  }

  const prevCatButton = document.getElementById(curr_cat + 'b');
  if (prevCatButton && curr_cat !== changeto) {
    prevCatButton.style.backgroundColor = 'white';
    prevCatButton.style.color = 'black';
    prevCatButton.style.borderColor = 'white';
    prevCatButton.style.boxShadow = '0px 0px 5px white';
  }

  const prevCatContent = document.getElementById(curr_cat);
  if (prevCatContent && curr_cat !== changeto) {
    prevCatContent.style.display = 'none';
  }

  const allItemsDiv = document.getElementById('allitems');
  if (allItemsDiv && changeto !== 'All') {
    allItemsDiv.style.display = 'none';
  } else if (allItemsDiv && changeto === 'All') {
    allItemsDiv.style.display = 'flex';
  }

  curr_cat = changeto;
}

document.addEventListener('DOMContentLoaded', () => {
  const initialButton = document.getElementById('Appetizersb');
  if (initialButton) {
    initialButton.style.backgroundColor = 'rgb(250, 244, 245)';
    initialButton.style.color = 'red';
    initialButton.style.borderColor = 'red';
    initialButton.style.boxShadow = '0px 0px 5px red';
  }

  const initialContent = document.getElementById('Appetizers');
  if (initialContent) {
    initialContent.style.display = 'flex';
  }

  const categories = ['Soups_salads', 'Rice_items', 'Breads_rotis', 'Special_curries', 'Side_dishes', 'Deserts', 'Drinks', 'All'];
  categories.forEach(cat => {
    if (cat !== 'Appetizers') {
      const catContent = document.getElementById(cat);
      if (catContent) {
        catContent.style.display = 'none';
      }
      const catButton = document.getElementById(cat + 'b');
      if (catButton && cat !== 'Appetizers') {
        catButton.style.backgroundColor = 'white';
        catButton.style.color = 'black';
        catButton.style.borderColor = 'white';
        catButton.style.boxShadow = '0px 0px 5px white';
      }
    }
  });
});
function cart(id, item, price) {
  var x = 0;
  total += parseInt(price);
  for (let i of cart_items) {
    if (i[0] == item) {
      i[3] += 1
      x = 1
      break;
    }
  }
  if (x != 1) { cart_items.push([id, item, parseInt(price), 1]) }
  updateCartUI();
}

function dec(button) {
  const cartItem = button.closest('.cartp');
  const qtyElem = cartItem.querySelector('.no_of');
  const priceElem = cartItem.querySelector('.price');
  const itemId = cartItem.querySelector('.id').innerText;
  const itemPrice = parseInt(priceElem.innerText.replace('₹', ''));

  let count = parseInt(qtyElem.innerText);
  if (count > 1) {
    let newCount = count - 1;
    qtyElem.innerText = newCount;
    for (let i = 0; i < cart_items.length; i++) {
      if (cart_items[i][0] == itemId) {
        cart_items[i][3] = newCount;
        break;
      }
    }
    updateTotal();
  } else {
    const indexToRemove = cart_items.findIndex(item => item[0] == itemId);
    if (indexToRemove > -1) {
      cart_items.splice(indexToRemove, 1);
      cartItem.remove(); // Remove the HTML element
      updateTotal();
      if (cart_items.length === 0) {
        const cartElement = document.getElementById('divcart');
        if (cartElement) {
          cartElement.innerHTML = '<p id="title">Cart items</p>'; // Reset to title
          cartElement.style.display = 'none';
        }
      }
    }
  }
}

function inc(button) {
  const cartItem = button.closest('.cartp');
  const qtyElem = cartItem.querySelector('.no_of');
  const itemId = cartItem.querySelector('.id').innerText;

  let count = parseInt(qtyElem.innerText);
  let newCount = count + 1;
  qtyElem.innerText = newCount;

  for (let i = 0; i < cart_items.length; i++) {
    if (cart_items[i][0] == itemId) {
      cart_items[i][3] = newCount;
      break;
    }
  }
  updateTotal();
}

function updateCartUI() {
  const cartElement = document.getElementById('divcart');
  cartElement.innerHTML = '<p id="title">Cart items</p>';
  total = 0;
  for (let i = 0; i < cart_items.length; i++) {
    total += cart_items[i][2] * cart_items[i][3];
    cartElement.innerHTML += `
      <div class="cartp">
        <p class="id" style="display:none;">${cart_items[i][0]}</p>
        <p class="name">${cart_items[i][1]}</p>
        <p class="price">${cart_items[i][2]}₹</p>
        <button class="min" onclick="dec(this)"><i class="fa-solid fa-minus"></i></button>
        <p class="no_of">${cart_items[i][3]}</p>
        <button class="plus" onclick="inc(this)"><i class="fa-solid fa-plus"></i></button>
      </div>`;
  }
  cartElement.innerHTML += `
    <div style="display:flex;justify-content:space-between;align-items:center;">
      <p class="namet">Total : </p><p class="pricet">${total}₹</p>
    </div>`;
  cartElement.style.display = cart_items.length > 0 ? 'flex' : 'none';
}

function updateTotal() {
  total = 0;
  for (let i = 0; i < cart_items.length; i++) {
    total += cart_items[i][2] * cart_items[i][3];
  }
  const totalElement = document.querySelector('#divcart .pricet');
  if (totalElement) {
    totalElement.innerText = `${total}₹`;
  }
}

function send() {
  let list_of_items = ''
  cart_items = cart_items.map((item) => [item[1], item[2], item[3]]);
  for (let i of cart_items) { list_of_items += ';' + i.toString() }
  var data = {
    items: list_of_items.slice(1)
  };
  $.ajax({
    url: 'http://127.0.0.1:5000/final/',
    type: 'GET',
    data: data,
    success: function (response) {
      console.log('Response from server:', response);
    },
    error: function (xhr, status, error) {
      console.log('An error occurred:', error);
    }
  });
}

function search() {
  let ser = document.getElementById('search').value.toLowerCase();

  if (ser === '') {
    document.getElementById('Appetizersb').style.backgroundColor = 'rgb(250, 244, 245)';
    document.getElementById('Appetizersb').style.color = 'red';
    document.getElementById('Appetizersb').style.borderColor = 'red';
    document.getElementById('Appetizersb').style.boxShadow = '0px 0px 5px red';
    document.getElementById('Appetizers').style.display = 'flex';
    document.getElementById('search_items').style.display = 'none';
    curr_cat = 'Appetizers';
  } else {
    var sortlist = [];
    for (let i of list) {
      let itemName = i[1].toLowerCase();
      if (itemName.startsWith(ser)) {
        sortlist.push(i);
      }
    }

    document.getElementById('search_items').style.display = 'flex';
    document.getElementById(curr_cat + 'b').style.backgroundColor = 'white';
    document.getElementById(curr_cat + 'b').style.color = 'black';
    document.getElementById(curr_cat + 'b').style.borderColor = 'white';
    document.getElementById(curr_cat + 'b').style.boxShadow = '0px 0px 5px white';
    document.getElementById(curr_cat).style.display = 'none';
    curr_cat = 'search_items';
    document.getElementById('search_items').innerHTML = '<p id="title">Search Results</p>';

    for (let i of sortlist) {
      const isUnavailable = i[4]?.toLowerCase() === 'unavailable';

      let itemHTML = `<div id="items" class="${isUnavailable ? 'unavailable' : ''}">
        <p class="item_id">${i[0]}</p>
        <p class="availability">${i[4]}</p>`;

      if (isUnavailable) {
        itemHTML += `<p class="item_message">This item is temporarily unavailable</p>`;
      }

      itemHTML += `
        <img id="img" src="/static/images/${i[3]}" alt="images/${i[3]}">
        <div>
          <p id="pname">${i[1]}</p>
          <p class="p"><span>Price&nbsp;:</span><span class="red">&nbsp;${i[2]}₹</span></p>
          <p class="p"><span>Rating:&nbsp;&nbsp;</span><span class="red">4.5&nbsp;&nbsp;</span><i class="fa-solid fa-star" id="star"></i></p>
        </div>`;

      if (!isUnavailable) {
        itemHTML += `<button onclick="cart('${i[0]}','${i[1]}','${i[2]}')">Add to cart</button>`;
      } else {
        itemHTML += `<button disabled class="disabled-button">Unavailable</button>`;
      }

      itemHTML += `</div>`;
      document.getElementById("search_items").innerHTML += itemHTML;
    }
  }
}

function log() {
  if (document.getElementById('loga').style.display === 'none' || document.getElementById('loga').style.display === '') { document.getElementById('loga').style.display = 'flex' }
  else { document.getElementById('loga').style.display = 'none' }
}

function rem() {
  document.getElementById('loga').style.display = 'none'
}

function cartdis() {
  if (document.getElementById('divcart').style.display === '' || document.getElementById('divcart').style.display === 'none') { document.getElementById('divcart').style.display = 'flex' }
  else { document.getElementById('divcart').style.display = 'none' }
}
appetizers = document.getElementById("Appetizers");
soups_salads = document.getElementById("Soups_salads");
rice_items = document.getElementById("Rice_items");
breads_rotis = document.getElementById("Breads_rotis");
special_curries = document.getElementById("Special_curries");
side_dishes = document.getElementById("Side_dishes");
deserts = document.getElementById("Deserts");
drinks = document.getElementById("Drinks");
menu = {
  appetizers: appetizers, soups_and_salads: soups_salads,
  rice_items: rice_items, breads_rotis: breads_rotis, special_curries: special_curries,
  side_dishes: side_dishes, deserts: deserts, drinks: drinks,
};

function update(data) {
  let div = menu[data.category]
  let divs = div.querySelectorAll('#items')
  let id1 = data.item[0][0].toString();
  for (let div of divs) {
    let id = div.querySelector(".item_id").innerHTML;
    if (id[0] == "'") { id = id.slice(1, -1) }
    if (id1 == id) {
      div.querySelector('#pname').innerHTML = data.item[0][1]
      div.querySelector('.red').innerHTML = `${data.item[0][2]}₹`
      if (data.item[0][4] == "Unavailable") {
        div.classList.add("mask");
        for (let i in cart_items) {
          if (id1 == cart_items[i][0]) {
            cart_items.splice(i, 1)
            let cartdiv = document.getElementById('cart')
            let cartdivs = cartdiv.querySelectorAll('#cartp')
            for (let x of cartdivs) {
              let cart_id = x.querySelector('#id').innerHTML
              if (id1 == cart_id) {
                x.style.textDecoration = "line-through";
                x.style.color = "red";
                x.title = 'This item is currently unavailable'
                total -= parseInt(x.querySelector('#price').innerHTML)
                document.getElementById('pricet').innerHTML = total
              }
            }
          }
        }
      }
      else { div.classList.remove("mask"); }
    }
  }

  div = document.getElementById('allitems')
  divs = div.querySelectorAll('#items')
  for (let div of divs) {
    id = div.querySelector('#pname').innerHTML
    if (id == data.item[0][1]) { div.classList.add('mask') }
    else { div.classList.remove('mask') }
  }
  for (let i of list) {
    if (i[1] == data.item[0][1]) { i[4] = data.item[0][4] }
  }
}

function del(data) {
  let div1 = menu[data.category];
  let divs = div1.querySelectorAll("#items");
  let id1 = data.item[0][0].toString();
  for (let div of divs) {
    let id = div.querySelector(".item_id").innerHTML;
    if (id[0] == "'") {
      id = id.slice(1, -1);
    }
    if (id1 == id) {
      div1.removeChild(div)
    }
  }
  for (let i in cart_items) {
    if (cart_items[i][0] == id1) {
      cart_items.splice(i, 1)
      let cartdiv = document.getElementById('cart')
      let cartdivs = cartdiv.querySelectorAll('#cartp')
      for (let x of cartdivs) {
        let cart_id = x.querySelector('#id').innerHTML
        if (id1 == cart_id) {
          console.log('equal')
          x.style.textDecoration = "line-through";
          x.style.color = "red";
          x.title = "This item is deleted from Menu";
          total -= parseInt(x.querySelector("#price").innerHTML);
          document.getElementById("pricet").innerHTML = total;
        }
      }
    }
  }
}

function add_item(data) {
  let div = menu[data.category];
  if (data.item[0][4] == "Unavailable") {
    div.innerHTML += `<div id="items" class="mask">
  <p class="item_id">${data.item[0][0]}</p>
        <p class="availability">${data.item[0][4]}</p>
        <p class="item_message">This item is temporarily unavailable</p>
            <img id="img" src="/static/images/${data.item[0][3]}" alt="images/${data.item[0][3]}">
            <div>
                <p id="pname">${data.item[0][1]}</p>
                <p class="p"><span>Price&nbsp;:</span><span class="red">&nbsp;${data.item[0][2]}₹</span></p>
                <p class="p"><span>Rating:&nbsp;&nbsp;</span><span class="red">4.5&nbsp;&nbsp;</span><i
                        class="fa-solid fa-star" id="star"></i></p>
            </div>
            <button onclick="cart('${data.item[0][1]}','${data.item[0][2]}')">Add to cart</button>
        </div>`;
  } else {
    div.innerHTML += `<div id="items" class="items">
        <p class="item_id">${data.item[0][0]}</p>
        <p class="availability">${data.item[0][4]}</p>
        <p class="item_message">This item is temporarily unavailable</p>
            <img id="img" src="/static/images/${data.item[0][3]}" alt="images/${data.item[0][3]}">
            <div>
                <p id="pname">${data.item[0][1]}</p>
                <p class="p"><span>Price&nbsp;:</span><span class="red">&nbsp;${data.item[0][2]}₹</span></p>
                <p class="p"><span>Rating:&nbsp;&nbsp;</span><span class="red">4.5&nbsp;&nbsp;</span><i
                        class="fa-solid fa-star" id="star"></i></p>
            </div>
            <button onclick="cart('${data.item[0][1]}','${data.item[0][2]}')">Add to cart</button>
        </div>
  `;
  }
  list.push(data.item)
  console.log(list)
}

const socket = new WebSocket("ws://" + window.location.host + "/ws/Menu/");
socket.onopen = function (e) {
  console.log("Connection established");
};

socket.onmessage = function (event) {
  let data = JSON.parse(event.data);
  data = data['message']['message']
  if (data['type'] == 'update') { update(data) }
  if (data['type'] == 'delete') { del(data) }
  if (data['type'] == 'new item') { add_item(data) }
};

socket.onclose = function (event) {
  if (event.wasClean) {
    console.log('Connection closed cleanly, code=' + event.code + ', reason=' + event.reason);
  } else {
    console.error('Connection died');
  }
};

socket.onerror = function (error) {
  console.error('WebSocket error:', error);
};

