document.addEventListener("DOMContentLoaded", function() {
    const submitButton = document.querySelector('button[type="submit"]');
    const originalButton = document.getElementById('original-encode')

    
    originalButton.addEventListener('click', async function(event) {
        event.preventDefault();

        const text = document.getElementById("text");
        const rows = document.getElementById("rows");
        const columns = document.getElementById("columns");
        const ciphertext = document.getElementById("ciphertext");

        // Проверка на пустую строку
        if (!text.value) {
            alert('Вы ввели пустую строку');
            return;
        }

        // Проверка корректности размеров матрицы
        if ((text.value.length) !== (rows.value * columns.value)) {
            console.log(text.value.length);
            alert("Введены неправильные размеры матрицы");
            return;
        }

        const data = {
            user_input: text.value,
            rows: parseInt(rows.value, 10),
            columns: parseInt(columns.value, 10)
        };

        try {
            // Отправляем асинхронный POST-запрос
            const response = await fetch('http://localhost:8080/original-encode-message/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(data)
            });

            // Проверка успешности запроса
            if (!response.ok) {
                throw new Error('Сетевая ошибка');
            }

            // Ждем и получаем данные в формате JSON
            const responseData = await response.json();
            console.log(responseData);

            // Показываем результат
            ciphertext.style.display = 'block';
            const ctext = ciphertext.querySelector('.ciphertext');
            // ctext.value = responseData.message;

            const ciphertextContainer = document.getElementById('ciphertext');
            ciphertextContainer.innerHTML += responseData.message;
            
        } catch (error) {
            console.error('Ошибка:', error);
        }
    });


    submitButton.addEventListener('click', async function(event) {
        event.preventDefault();

        const text = document.getElementById("text");
        const rows = document.getElementById("rows");
        const columns = document.getElementById("columns");
        const ciphertext = document.getElementById("ciphertext");

        // Проверка на пустую строку
        if (!text.value) {
            alert('Вы ввели пустую строку');
            return;
        }

        // Проверка корректности размеров матрицы
        if ((text.value.length) !== (rows.value * columns.value)) {
            console.log(text.value.length);
            alert("Введены неправильные размеры матрицы");
            return;
        }

        const data = {
            user_input: text.value,
            rows: parseInt(rows.value, 10),
            columns: parseInt(columns.value, 10)
        };

        try {
            // Отправляем асинхронный POST-запрос
            const response = await fetch('http://localhost:8080/encode-messages/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(data)
            });

            // Проверка успешности запроса
            if (!response.ok) {
                throw new Error('Сетевая ошибка');
            }

            // Ждем и получаем данные в формате JSON
            const responseData = await response.json();
            console.log(responseData);

            // Показываем результат
            ciphertext.style.display = 'block';
            const ctext = ciphertext.querySelector('.ciphertext');
            // ctext.value = responseData.message;

            const ciphertextContainer = document.getElementById('ciphertext');
            ciphertextContainer.innerHTML += responseData.message;
            
        } catch (error) {
            console.error('Ошибка:', error);
        }
    });
});
