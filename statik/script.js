document.addEventListener("DOMContentLoaded", async () => {
  const container = document.getElementById("product-list");

  const res = await fetch("/api/products");
  const products = await res.json();

  products.forEach((p) => {
    const div = document.createElement("div");
    div.className = "product";
    div.innerHTML = `
      <h2>${p.name}</h2>
      <img src="${p.image}" alt="${p.name}" />
      <p>Ціна: ${p.price} грн</p>
      <input type="email" placeholder="Ваш email" />
      <button>Замовити</button>
    `;

    div.querySelector("button").addEventListener("click", async () => {
      const email = div.querySelector("input").value;
      if (!email) return alert("Введіть email");

      const res = await fetch("/api/order", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ email, product_id: p.id }),
      });

      const data = await res.json();
      alert(data.message);
    });

    container.appendChild(div);
  });
});