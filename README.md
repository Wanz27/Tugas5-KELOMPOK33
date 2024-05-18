body {
    font-family: 'Raleway', sans-serif;
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

*,
*::before,
*::after {
    box-sizing: inherit;
}

header {
    background: #0ec9e2;
    padding: 16px;
    color: white;
    text-align: center;
}

.wrapper {
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 16px;
}

.wrapper .container {
    width: 100%;
    max-width: 1024px;
    border-radius: 8px;
    margin: 16px 0;
    background: #0da3e4;
    padding: 16px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

.form {
    display: flex;
    flex-direction: column;
    padding: 16px;
    border-radius: 16px;
    background: white;
    box-shadow: 0 4px 8px rgba(242, 238, 6, 0.894);
}

.form-group {
    display: flex;
    flex-direction: column;
    margin-bottom: 16px;
}

.form-group label {
    margin-bottom: 4px;
    font-size: 18px;
    font-weight: lighter;
}

input[type=text],
input[type=date],
select {
    font-family: 'Raleway', sans-serif;
    background: #F5F1FF;
    border: 2px solid #ee8e21;
    border-radius: 8px;
    padding: 16px;
    margin-bottom: 8px;
    font-size: 16px;
}

input[type=text]::placeholder,
input[type=date]::placeholder {
    color: #ccc;
}

.btn-submit {
    width: fit-content;
    border: none;
    font-family: 'Raleway', sans-serif;
    border-radius: 16px;
    padding: 12px 24px;
    background: white;
    border: 2px solid #ee8e21;
    color: black;
    font-size: 16px;
    cursor: pointer;
    align-self: flex-end;
    transition: background 0.3s, color 0.3s;
}

.btn-submit:hover {
    background: #ee8e21;
    color: white;
}

input[type=text]:focus,
input[type=date]:focus,
select:focus,
.btn-submit:focus {
    outline: none;
}

.text-center {
    text-align: center;
}

.form-book {
    margin: auto 0;
}

@media only screen and (max-width: 1024px) {
    .wrapper {
        padding: 8px;
    }

    .wrapper .container {
        width: 100%;
        padding: 16px;
    }

    .form {
        width: 100%;
        padding: 16px;
    }
}

