from flask import Flask

app = Flask(__name__)


@app.route('/')
def juego():
    return """
    <!DOCTYPE html>
    <html lang="es">

    <head>
        <meta charset="UTF-8">
        <title>Mi Mascota Virtual</title>

        <style>

            body {
                font-family: Arial, sans-serif;
                background: linear-gradient(135deg, #d9f3ff, #f5ddff);
                text-align: center;
                margin: 0;
                padding: 30px;
            }

            .juego {
                background-color: white;
                max-width: 600px;
                margin: auto;
                padding: 30px;
                border-radius: 25px;
                box-shadow: 0 10px 30px rgba(0,0,0,0.15);
            }

            h1 {
                color: #6846d8;
            }

            .mascota {
                font-size: 140px;
                margin: 20px;
                animation: saltar 2s infinite;
            }

            @keyframes saltar {
                0%, 100% {
                    transform: translateY(0);
                }

                50% {
                    transform: translateY(-10px);
                }
            }

            .estado {
                margin: 20px 0;
            }

            .barra {
                background-color: #eeeeee;
                width: 100%;
                height: 25px;
                border-radius: 20px;
                margin-bottom: 15px;
                overflow: hidden;
            }

            .relleno {
                height: 100%;
                border-radius: 20px;
            }

            .hambre {
                background-color: #ff9f43;
            }

            .felicidad {
                background-color: #ff6b9d;
            }

            .energia {
                background-color: #54a0ff;
            }

            button {
                border: none;
                padding: 15px 20px;
                margin: 8px;
                border-radius: 12px;
                font-size: 17px;
                cursor: pointer;
                color: white;
            }

            .comida {
                background-color: #ff9f43;
            }

            .jugar {
                background-color: #ff6b9d;
            }

            .dormir {
                background-color: #54a0ff;
            }

            button:hover {
                transform: scale(1.05);
            }

            #mensaje {
                font-size: 20px;
                font-weight: bold;
                color: #6846d8;
                min-height: 30px;
            }

        </style>
    </head>

    <body>

        <div class="juego">

            <h1>🐣 Mi Mascota Virtual</h1>

            <p>¡Cuida a tu mascota!</p>

            <div class="mascota" id="mascota">
                🐣
            </div>

            <div class="estado">

                <p>🍎 Hambre: <span id="numeroHambre">70</span>%</p>

                <div class="barra">
                    <div id="barraHambre"
                         class="relleno hambre"
                         style="width: 70%;">
                    </div>
                </div>


                <p>💖 Felicidad: <span id="numeroFelicidad">70</span>%</p>

                <div class="barra">
                    <div id="barraFelicidad"
                         class="relleno felicidad"
                         style="width: 70%;">
                    </div>
                </div>


                <p>⚡ Energía: <span id="numeroEnergia">70</span>%</p>

                <div class="barra">
                    <div id="barraEnergia"
                         class="relleno energia"
                         style="width: 70%;">
                    </div>
                </div>

            </div>


            <div>

                <button class="comida" id="botonComida">
                    🍎 Dar comida
                </button>

                <button class="jugar" id="botonJugar">
                    🎮 Jugar
                </button>

                <button class="dormir" id="botonDormir">
                    😴 Dormir
                </button>

            </div>


            <p id="mensaje">
                ¡Hola! Soy tu mascota 💜
            </p>

        </div>


        <script>

            let hambre = 70;
            let felicidad = 70;
            let energia = 70;


            function actualizar() {

                document.getElementById("numeroHambre").textContent = hambre;
                document.getElementById("numeroFelicidad").textContent = felicidad;
                document.getElementById("numeroEnergia").textContent = energia;

                document.getElementById("barraHambre").style.width =
                    hambre + "%";

                document.getElementById("barraFelicidad").style.width =
                    felicidad + "%";

                document.getElementById("barraEnergia").style.width =
                    energia + "%";
            }


            document.getElementById("botonComida").addEventListener("click", function() {

                hambre += 20;

                if (hambre > 100) {
                    hambre = 100;
                }

                document.getElementById("mensaje").textContent =
                    "🍎 ¡Qué rico! Gracias por la comida.";

                actualizar();
            });


            document.getElementById("botonJugar").addEventListener("click", function() {

                if (energia >= 20) {

                    felicidad += 20;
                    energia -= 20;
                    hambre -= 10;

                    if (felicidad > 100) {
                        felicidad = 100;
                    }

                    if (hambre < 0) {
                        hambre = 0;
                    }

                    document.getElementById("mensaje").textContent =
                        "🎮 ¡Me divertí mucho!";

                } else {

                    document.getElementById("mensaje").textContent =
                        "😴 Estoy cansado, necesito dormir.";

                }

                actualizar();
            });


            document.getElementById("botonDormir").addEventListener("click", function() {

                energia += 30;

                if (energia > 100) {
                    energia = 100;
                }

                document.getElementById("mensaje").textContent =
                    "😴 Zzz... ¡Ya tengo más energía!";

                actualizar();
            });


            actualizar();

        </script>

    </body>

    </html>
    """


if __name__ == '__main__':
    app.run(debug=True)