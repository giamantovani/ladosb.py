

const cart = [];

function addToCart(vinylId) {
    const vinyl = vinyls.find(v => v.id === vinylId);
    cart.push(vinyl);
    alert(`${vinyl.title} ha sido añadido al carrito.`);
    updateCart();
}

function updateCart() {
    const cartContainer = document.getElementById('cart');
    cartContainer.innerHTML = '';
    cart.forEach(item => {
        const cartItem = document.createElement('div');
        cartItem.textContent = `${item.title} - $${item.price}`;
        cartContainer.appendChild(cartItem);
    });
}

document.addEventListener('DOMContentLoaded', () => {
    const carouselInner = document.getElementById('carousel-inner');

    function loadDiscos() {
        fetch('/compra/discos/') 
            .then(response => response.json())
            .then(data => {
                const discos = data.slice(0, 8);
                
                for (let i = 0; i < discos.length; i += 4) {
                    const slideDiscos = discos.slice(i, i + 4);
                    const isActive = i === 0 ? 'active' : ''; 
                    let slideContent = `<div class="carousel-item ${isActive}"><div class="row">`;

                    slideDiscos.forEach(disco => {
                        slideContent += `
                            <div class="col-3 vinyl-item">
                                <div class="card">
                                    <img src="${disco.imagen}" class="card-img-top" alt="${disco.titulo}">
                                    <div class="card-body">
                                        <h5 class="card-title">${disco.titulo}</h5>
                                        <p class="card-text">${disco.artista}</p>
                                        <p class="card-text">${disco.descripcion}</p>
                                        <button class="btn btn-danger" onclick="addToCart(${disco.id})">Comprar</button>
                                        <a href="/disco/${disco.id}" class="btn btn-dark">Ver Detalles</a>
                                    </div>
                                </div>
                            </div>
                        `;
                    });

                    slideContent += '</div></div>';
                    carouselInner.innerHTML += slideContent;
                }
            })
            .catch(error => {
                console.error('Error al cargar discos:', error);
            });
    }

    loadDiscos();
});

