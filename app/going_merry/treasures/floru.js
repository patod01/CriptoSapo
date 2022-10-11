// cables go here
const local_IP = 'localhost';
let clicker = 0;

const titulo = document.querySelector('.title');
titulo.onclick = () => {
     titulo.innerHTML = clicker;
     clicker++;
}

function api_shortcut(method, action) {
     const options = {
          method: `${method}`,
          headers: {'Content-Type': 'application/json'},
          body: `{"action":"${action}"}`
     };
     fetch(`http://${local_IP}:7777/wallet/`, options)
          .then(response => response.json())
          .then(response => console.log(response))
          .catch(err => console.error(err));
}

const b_buy = document.querySelector('.buy');
b_buy.onclick = () => api_shortcut('POST', 'buy');

const b_sell = document.querySelector('.sell');
b_sell.onclick = () => api_shortcut('POST', 'sell');

const b_ship = document.querySelector('.ship');
b_ship.onclick = () => api_shortcut('POST', 'ship');

const b_spy = document.querySelector('.spy');
b_spy.onclick = () => api_shortcut('POST', 'spy');

// const b_del = document.querySelector('.del');
// b_del.onclick = () => api_shortcut('DELETE', 'del');
