from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.keys import Keys
from Services.WebDriverManager import WebDriverManager
from datetime import datetime


class FuncionesModular:
    def __init__(self, url):
        self.web_driver = WebDriverManager(url)
        self.start_time = None
        self.start_datetime = None

    def reporteInicial(self):
        self.start_time = time.time()
        self.start_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"Script iniciado a las: {self.start_datetime}")

    def reporteFinal(self):
        end_time = time.time()
        end_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"Script finalizado a las: {end_datetime}")

        execution_time = end_time - self.start_time
        print(f"El script tardó {execution_time:.2f} segundos en ejecutarse.")

    def sucursal(self, prov, seller, direccion_email):
        sel = '//span[contains(text(), "Seleccioná el método de entrega")]/ancestor::div[@role="button"]'
        tienda = '//p[contains(text(), "Retiro en tienda")]'
        confirmar = '//button/div[contains(text(), "Confirmar")]/ancestor::button'
        spinner = ".vtex__icon-spinner"
        button_screen = '//button[@id="onesignal-slidedown-cancel-button"]'
        email = '//input[@type="email"]'
        enviar_button = '//button/div[contains(text(), "Enviar")]'
        region_select = "//label[.//span[contains(text(), \"Provincia / Región\")]]//select"
        tienda_select = "//label[.//span[contains(text(), \"Tienda\")]]//select"
        print("Inicia Sucursales...")
        try:
            # self.web_driver.click(By.XPATH, sel)
            self.web_driver.click(By.LINK_TEXT, "Seleccioná el método de entrega")
            self.web_driver.send_keys(By.XPATH, email, direccion_email)
            self.web_driver.click(By.XPATH, enviar_button)
            self.web_driver.click(By.XPATH, tienda)
            self.web_driver.find_element(
                By.XPATH, "//label[.//span[contains(text(), \"Provincia / Región\")]]//select").click()
            driver = self.web_driver.get_driver()
            dropdown = driver.find_element(
                By.CSS_SELECTOR, ".b--muted-2 > .o-0")
            dropdown.find_element(By.XPATH, f"//option[. = '{prov}']").click()
            self.web_driver.find_element(
                By.XPATH, "//label[.//span[contains(text(), \"Tienda\")]]//select").click()
            dropdown = driver.find_element(
                By.CSS_SELECTOR, ".b--muted-2 > .o-0")
            dropdown.find_element(
                By.XPATH, f"//option[. = '{seller}']").click()
            self.web_driver.click(By.XPATH, confirmar)
            texto = self.web_driver.wait_appear(
                By.XPATH, '//span[contains(text(), "¡Listo, guardamos tu configuración!")]')
            texto = texto.text
            time.sleep(1)
            self.web_driver.click(
                By.CLASS_NAME, "vtex-modal-layout-0-x-closeIcon")
            return texto
        except Exception as e:
            print(e)

    def sucursalClienteNuevo(self, prov, seller, direccion_email):
        sel = "//span[contains(.,'Seleccioná el método de entrega')]"
        input_mail = "//input[contains(@type,'email')]"
        btn_continuar = "//button/div[contains(text(), 'Enviar')]"
        retiro = '//p[contains(text(), "Retiro en tienda")]'
        provincia = "//label[.//span[contains(text(), 'Provincia / Región')]]//select"
        sele_prov = f"//option[. = '{prov}']"
        tienda = "//label[.//span[contains(text(), 'Tienda')]]//select"
        sele_tienda = f"//option[. = '{seller}']"
        confirmar = "//button/div[contains(text(), 'Confirmar')]/ancestor::button"
        closemodal = "vtex-modal-layout-0-x-closeIcon"
        print("ingresando en Modal de Geolocalizacion")
        self.web_driver.click(By.XPATH, sel)
        self.web_driver.click(By.XPATH, input_mail)
        self.web_driver.send_keys(By.XPATH, input_mail, direccion_email)
        self.web_driver.click(By.XPATH, btn_continuar)
        self.web_driver.click(By.XPATH, retiro)
        self.web_driver.select_dropdown(By.XPATH, provincia, prov)
        self.web_driver.click(By.XPATH, sele_prov)
        self.web_driver.select_dropdown(By.XPATH, tienda, seller)
        self.web_driver.click(By.XPATH, sele_tienda)
        self.web_driver.click(By.XPATH, confirmar)
        time.sleep(3)
        self.web_driver.click(By.CLASS_NAME, closemodal)

    def direccion1(self, mail):
        sel = "//span[contains(text(), 'Seleccioná el método de entrega')]"
        insert = "//input[@type='email']"
        sigui = "//div/button//div[contains(text(), 'Enviar')]"
        acept = "//div/button//div[contains(text(), 'Confirmar')]"
        closemodal = "vtex-modal-layout-0-x-closeIcon"
        print("ingresando en Modal de Geolocalizacion")
        self.web_driver.click(By.XPATH, sel)
        time.sleep(2)
        self.web_driver.click(By.XPATH, insert)
        self.web_driver.send_keys(By.XPATH, insert, mail)
        self.web_driver.click(By.XPATH, sigui)
        self.web_driver.click(By.XPATH, acept)
        time.sleep(4)
        self.web_driver.click(By.CLASS_NAME, closemodal)

    def direccionNueva(self, mail, direccion):
        sel = "//span[contains(text(), 'Seleccioná el método de entrega')]"
        insert = "//input[@type='email']"
        sigui = "//div/button//div[contains(text(), 'Enviar')]"
        inputdire = "//*[@id='autocomplete']"
        checkboxbc = "//div/label[contains(text(), '¿Vivís en barrio cerrado?')]"
        acept = "//div/button//div[contains(text(), 'Confirmar')]"
        closemodal = "vtex-modal-layout-0-x-closeIcon"
        self.web_driver.click(By.XPATH, sel)
        self.web_driver.click(By.XPATH, insert)
        self.web_driver.send_keys(By.XPATH, insert, mail)
        self.web_driver.click(By.XPATH, sigui)
        self.web_driver.send_keys(By.XPATH, inputdire, direccion)
        lugar = self.web_driver.find_element(By.XPATH, inputdire)
        if lugar is not None:
            lugar.send_keys(direccion)
            time.sleep(1)
            lugar.send_keys(Keys.ARROW_DOWN)
            time.sleep(1)
            lugar.send_keys(Keys.ENTER)
        self.web_driver.click(By.XPATH, checkboxbc)
        self.web_driver.click(By.XPATH, acept)
        time.sleep(5)
        self.web_driver.click(By.CLASS_NAME, closemodal)

    def direccionNuevaDV1(self, mail, direccion):
        sel = "//span[contains(text(), 'Seleccioná el método de entrega')]"
        insert = "//input[@type='email']"
        sigui = "//div/button//div[contains(text(), 'Enviar')]"
        inputdire = "//*[@id='autocomplete']"
        self.web_driver.click(By.XPATH, sel)
        self.web_driver.click(By.XPATH, insert)
        self.web_driver.send_keys(By.XPATH, insert, mail)
        self.web_driver.click(By.XPATH, sigui)
        self.web_driver.send_keys(By.XPATH, inputdire, direccion)
        time.sleep(2)

    def nextdir(self):
        seldire = "//*[@id='results']/div[1]"
        time.sleep(1)
        self.web_driver.click(By.XPATH, seldire)

    def direcconNuevaDV2(self):
        checkboxbc = "//div/label[contains(text(), '¿Vivís en barrio cerrado?')]"
        acept = "//div/button//div[contains(text(), 'Confirmar')]"
        closemodal = "vtex-modal-layout-0-x-closeIcon"
        self.web_driver.click(By.XPATH, checkboxbc)
        self.web_driver.click(By.XPATH, acept)
        time.sleep(5)
        self.web_driver.click(By.CLASS_NAME, closemodal)

    def ModalFueraDeCobertura(self, mail, adress):
        sel = "//span[contains(text(), 'Seleccioná el método de entrega')]"
        insert = "//input[@type='email']"
        sigui = "//div/button//div[contains(text(), 'Enviar')]"
        aggAdress = "//div[contains(text(),'Agregar nueva dirección')]"
        aggAdress2 = "//div[contains(text(),'Agregar otra dirección')]"
        inputAdress = "//input[contains(@id,'autocomplete')]"
        resuls = "//*[@id='results']/div[1]/div/span"
        btNext = "//div[contains(text(),'Confirmar')]"
        btNext2 = "//div[contains(text(),'Continuar Comprando')]"
        btnNext4 = "//div[contains(text(),'Mi compra es Electro')]"
        btNext3 = "//span[contains(text(),'Empezar a comprar')]"
        self.web_driver.click(By.XPATH, sel)
        self.web_driver.click(By.XPATH, insert)
        self.web_driver.send_keys(By.XPATH, insert, mail)
        self.web_driver.click(By.XPATH, sigui)
        try:
            self.web_driver.move(By.XPATH, aggAdress)
            self.web_driver.click(By.XPATH, aggAdress)
        except:
            self.web_driver.move(By.XPATH, aggAdress2)
            self.web_driver.click(By.XPATH, aggAdress2)
        self.web_driver.click(By.XPATH, inputAdress)
        self.web_driver.send_keys(By.XPATH, inputAdress, adress)
        time.sleep(1)
        try:
            self.web_driver.click(By.XPATH, resuls)
        except:
            self.web_driver.send_keys(By.XPATH, inputAdress, Keys.ARROW_DOWN)
            time.sleep(1)
            self.web_driver.send_keys(By.XPATH, inputAdress, Keys.ENTER)
            time.sleep(1)
        time.sleep(3)
        self.web_driver.move(By.XPATH, btNext)
        self.web_driver.click(By.XPATH, btNext)
        try:
            self.web_driver.click(By.XPATH, btNext2)
        except:
            self.web_driver.click(By.XPATH, btnNext4)
        try:
            self.web_driver.click(By.XPATH, btNext3)
        except:
            time.sleep(6)

    def cerrarModal(self):
        xpathCerrar = "//a[contains(text(), 'Ahora no')]"
        self.web_driver.click(By.XPATH, xpathCerrar)

    def buscarArticulo(self, name):
        xpathBuscador = "//*[@id='downshift-0-input']"
        print('Clickeando Buscador. Cuac')
        try:
            self.web_driver.click(By.XPATH, xpathBuscador)
            self.web_driver.send_keys(By.XPATH, xpathBuscador, name)
            self.web_driver.send_keys(By.XPATH, xpathBuscador, Keys.ENTER)
            texto = self.web_driver.wait_appear(
                By.XPATH, f'//h1[contains(text(), "{name.lower()}")]')
            return texto.text
        except Exception as e:
            print(e)

    def addToCart(self):
        xpathContainer = '//div[contains(@class, "vtex-addToCart-container")]'
        for i in range(3):
            try:
                self.web_driver.click(By.XPATH, xpathContainer)
                break
            except StaleElementReferenceException:
                self.web_driver.click(By.XPATH, xpathContainer)

    def ingresarPdp1(self):
        xpathPDP = "//*[@id='gallery-layout-container']/div[1]"
        self.web_driver.click(By.XPATH, xpathPDP)

    def cargarArticuloPDP(self):
        xpathAgregar = "//div//button[contains(@class, 'vtex-addToCart-button jumboargentinaio-store-theme-3tBLXsLwJbhSbe3mbcah1x ')]"
        self.web_driver.click(By.XPATH, xpathAgregar)

    def cargarArticuloPLP(self, div_num: int, cant: int = 1):
        xpathContainer = f'//div[contains(@class, "vtex-addToCart-container")]'
        xpathBotonAgregaraCarrito = xpathContainer + f'[{div_num}]'
        print(f'Agregando articulo de PLP numero {div_num} al carrito')
        self.web_driver.wait_appear(By.XPATH, xpathContainer)
        self.web_driver.wait_appear(By.XPATH, xpathBotonAgregaraCarrito)
        self.web_driver.click(By.XPATH, xpathBotonAgregaraCarrito)
        for i in range(cant - 1):
            mas = "//*[@id='gallery-layout-container']/div[1]/section/a/article/div[6]/div/button[2]/i"
            self.web_driver.wait_appear(By.XPATH, mas)
            self.web_driver.click(By.XPATH, mas)

    def ingresarCarritoyConfirmar(self):
        xpathCarrito = "//div/aside[contains(@class, 'vtex-minicart-2-x-minicartWrapperContainer')]"
        # xpathCarrito = '/html/body/div[2]/div/div[1]/div/div[5]/div[1]/div/div/div[2]/section/div/div[7]/aside/div/div/button'
        xpathConfirmarCarrito = "//button[contains(@class, 'jumboargentinaio-store-theme-2ylCKZyu_FDK_wbNrY3ZvH ')]"
        print('Haciendo Click en el carrito')
        self.web_driver.wait_appear(By.XPATH, xpathCarrito)
        self.web_driver.click(By.XPATH, xpathCarrito)
        self.web_driver.wait_appear(By.XPATH, xpathConfirmarCarrito)
        self.web_driver.click(By.XPATH, xpathConfirmarCarrito)

    def irACheckout(self):
        xpathContinuar = "(//button[contains(@title,'Comprar ahora')])[2]"
        time.sleep(2)
        self.web_driver.click2(By.XPATH, xpathContinuar)
        print("ir a checkout")

    def goCart(self):
        xpathCarrito = "//div/aside[contains(@class, 'vtex-minicart-2-x-minicartWrapperContainer')]"
        # xpathCarrito = '/html/body/div[2]/div/div[1]/div/div[5]/div[1]/div/div/div[2]/section/div/div[7]/aside/div/div/button'
        for i in range(3):
            try:
                self.web_driver.click(By.XPATH, xpathCarrito)

                break
            except StaleElementReferenceException:
                self.web_driver.click(By.XPATH, xpathCarrito)

    def criterio(self, option):
        xpathStep1 = "//button[@kind='inline'][contains(.,'Saltar')]"
        xpathStep2 = "//span[@class='css-xspcod'][contains(.,'El sitio es muy lento')]"
        xpathStep3 = "//button[@type='button'][contains(.,'Siguiente')]"
        xpathStep4 = "//button[@type='button'][contains(.,'Cerrar')]"
        xpathCriterio = f"//label[contains(text(), '{option}')]"
        xpathFinalizar = "//*[@id='cart-to-orderform']"
        try:
            self.web_driver.click(By.XPATH, xpathStep1)
            self.web_driver.click(By.XPATH, xpathStep2)
            self.web_driver.click(By.XPATH, xpathStep3)
            self.web_driver.click(By.XPATH, xpathStep4)
        except:
            time.sleep(1)
        try:
            self.web_driver.click(By.XPATH, xpathCriterio)
        except:
            self.web_driver.refresh()
        try:
            self.web_driver.click(By.XPATH, xpathStep1)
            self.web_driver.click(By.XPATH, xpathStep2)
            self.web_driver.click(By.XPATH, xpathStep3)
            self.web_driver.click(By.XPATH, xpathStep4)
        except:
            time.sleep(1)
        self.web_driver.click(By.XPATH, xpathCriterio)
        time.sleep(2)
        self.web_driver.click(By.XPATH, xpathFinalizar)

    def ingresoMail(self, email):
        xpathCuadroMail = "//*[@id='client-pre-email']"
        xpathNext = "//*[@id='btn-client-pre-email']"
        self.web_driver.click(By.XPATH, xpathCuadroMail)
        self.web_driver.send_keys(By.XPATH, xpathCuadroMail, email)
        self.web_driver.click(By.XPATH, xpathNext)

    def click_and_write(self, xpath, text):
        self.web_driver.click(By.XPATH, xpath)
        self.web_driver.send_keys(By.XPATH, xpath, text)

    def write(self, xpath, text):
        self.web_driver.wait_appear(By.XPATH, xpath)
        self.web_driver.send_keys_delay(By.XPATH, xpath, text, delay=0.3)

    def identificacion(self, nombre, apellidos, fecha, area, numero, dni):
        name = "//*[@id='client-first-name']"
        nickname = "//*[@id='client-last-name']"
        fnaci = "//*[@id='client-birthday']"
        cod_area = "//*[@id='client-phone1']"
        cod_numero = "//*[@id='client-phone3']"
        doc_type = "//*[@id='client-document-types']"
        dni_xpath = "//*[@id='client-document']"
        self.write(name, nombre)
        time.sleep(1)
        self.write(nickname, apellidos)
        time.sleep(1)
        self.write(fnaci, fecha)
        time.sleep(1)
        self.web_driver.select_by_value(By.XPATH, doc_type, "DNI")
        time.sleep(1)
        self.write(dni_xpath, dni)
        time.sleep(1)
        self.write(cod_area, area)
        time.sleep(1)
        self.write(cod_numero, numero)
        time.sleep(1)
        self.write(name, nombre)
        time.sleep(1)
        self.write(nickname, apellidos)
        time.sleep(1)

    def aceptar_terminosycondiciones(self):
        self.web_driver.click(
            By.XPATH, "//p[contains(@class, 'terms-condiciones')]")

    def cerrar_politicas(self):
        xpath_X = "//div[contains(@class, 'ppd-container')]/p"
        self.web_driver.wait_appear(By.XPATH, xpath_X)
        self.web_driver.click(By.XPATH, xpath_X)

    def goto_deliver(self):
        self.web_driver.click(By.XPATH, "//button[@id='new-button-profile']")

    def agregar_direccion(self):
        button = "//button[@id='customButtonAddress']"
        self.web_driver.wait_appear(By.XPATH, button)
        self.web_driver.click(By.XPATH, button)

    def genero(self, genero_masculino: bool):
        xpath_holder = "//*[@id='client-profile-data']/div/div[2]/div/div/form/div/div/fieldset[1]/p[10]/"
        masculino = xpath_holder + "label[1]/span"
        femenino = xpath_holder + "label[2]/span/span"
        if genero_masculino:
            self.web_driver.click(By.XPATH, masculino)
        else:
            self.web_driver.click(By.XPATH, femenino)

    def envioRecurrenteDomicilio(self):
        xpathEnvio = "//div[contains(@class, 'shipping-method--item')]"
        xpathfecha = "(//i[contains(@data-colindex,'1')])[1]"
        xpathfecha2 = "(//i[contains(@data-colindex,'3')])[1]"
        xpathfecha3 = "(//i[contains(@data-colindex,'5')])[1]"
        ir_a_pago_xpath = "//button[contains(@class, 'shipping-step--finish')]"
        btnpay = "//*[@id='payment-data-submit']/span"
        self.web_driver.click(By.XPATH, xpathEnvio)
        time.sleep(1)
        try:
            self.web_driver.move(By.XPATH, xpathfecha)
            self.web_driver.click(By.XPATH, xpathfecha)
        except:
            try:
                self.web_driver.move(By.XPATH, xpathfecha2)
                self.web_driver.click(By.XPATH, xpathfecha2)
            except:
                self.web_driver.move(By.XPATH, xpathfecha3)
                self.web_driver.click(By.XPATH, xpathfecha3)
        time.sleep(1)
        self.web_driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);")
        self.web_driver.click(By.XPATH, ir_a_pago_xpath)
        self.web_driver.move(By.XPATH, btnpay)
        print('Script culminado con éxito')
        time.sleep(10)

    def envioRecurrenteTienda(self):
        xpathRetiro = "//*[@id='Retiro en tienda']"
        xpathTienda = "//div[contains(@class, 'shipping-method--content')]"
        xpathfecha = "(//i[contains(@data-colindex,'1')])[1]"
        xpathfecha2 = "(//i[contains(@data-colindex,'3')])[1]"
        xpathfecha3 = "(//i[contains(@data-colindex,'5')])[1]"
        ir_a_pago_xpath = "//button[contains(@class, 'shipping-step--finish')]"
        btnpay = "//*[@id='payment-data-submit']/span"
        self.web_driver.click(By.XPATH, xpathRetiro)
        self.web_driver.click(By.XPATH, xpathTienda)
        time.sleep(1)
        try:
            self.web_driver.move(By.XPATH, xpathfecha)
            self.web_driver.click(By.XPATH, xpathfecha)
        except:
            try:
                self.web_driver.move(By.XPATH, xpathfecha2)
                self.web_driver.click(By.XPATH, xpathfecha2)
            except:
                self.web_driver.move(By.XPATH, xpathfecha3)
                self.web_driver.click(By.XPATH, xpathfecha3)
        time.sleep(1)
        self.web_driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);")
        self.web_driver.click(By.XPATH, ir_a_pago_xpath)
        self.web_driver.move(By.XPATH, btnpay)
        print('Script culminado con éxito')
        time.sleep(10)

    def envioRecurrenteTiendaElectro(self):
        xpathRetiro = "//div//p//strong[contains(text(), 'Envío a Domicilio 24 Horas en Capital Federal y Gran Buenos Aires. - Electro')]"
        xpathRetiro2 = "//div//p//strong[contains(text(), 'Envio Domicilio Nacional Electros Grandes')]"
        xpathfecha = "(//i[contains(@data-colindex,'1')])[1]"
        xpathfecha2 = "(//i[contains(@data-colindex,'3')])[1]"
        xpathfecha3 = "(//i[contains(@data-colindex,'5')])[1]"
        ir_a_pago_xpath = "//button[contains(@class, 'shipping-step--finish')]"
        btnpay = "//*[@id='payment-data-submit']/span"
        try:
            self.web_driver.click(By.XPATH, xpathRetiro)
        except:
            self.web_driver.click(By.XPATH, xpathRetiro2)
        try:
            self.web_driver.move(By.XPATH, xpathfecha)
            self.web_driver.click(By.XPATH, xpathfecha)
        except:
            try:
                self.web_driver.move(By.XPATH, xpathfecha2)
                self.web_driver.click(By.XPATH, xpathfecha2)
            except:
                self.web_driver.move(By.XPATH, xpathfecha3)
                self.web_driver.click(By.XPATH, xpathfecha3)
        time.sleep(1)
        self.web_driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);")
        self.web_driver.click(By.XPATH, ir_a_pago_xpath)
        self.web_driver.move(By.XPATH, btnpay)
        print('Script culminado con éxito')
        time.sleep(10)

    def envioClienteNuevo(self):
        xpathfecha = "(//i[contains(@data-colindex,'1')])[1]"
        xpathfecha2 = "(//i[contains(@data-colindex,'3')])[1]"
        xpathfecha3 = "(//i[contains(@data-colindex,'5')])[1]"
        ir_a_pago_xpath = "//button[contains(@class, 'shipping-step--finish')]"
        btnpay = "//*[@id='payment-data-submit']/span"
        try:
            self.web_driver.move(By.XPATH, xpathfecha)
            self.web_driver.click(By.XPATH, xpathfecha)
        except:
            try:
                self.web_driver.move(By.XPATH, xpathfecha2)
                self.web_driver.click(By.XPATH, xpathfecha2)
            except:
                self.web_driver.move(By.XPATH, xpathfecha3)
                self.web_driver.click(By.XPATH, xpathfecha3)
        time.sleep(1)
        self.web_driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);")
        self.web_driver.click(By.XPATH, ir_a_pago_xpath)
        self.web_driver.move(By.XPATH, btnpay)
        print('Script culminado con éxito')
        time.sleep(10)

    def envioClienteNuevo_Direccion(self, direccion, tienda):
        btnAdress = "//button[contains(@id,'customButtonAddress')]"
        inputAdress = "//input[contains(@id,'autocomplete')]"
        results = "//*[@id='results']/div[1]/div/span"
        inputBcerrado = "//div//label[contains(text(), '¿Vivís en barrio cerrado?')]"
        btnContinuar = "//div[contains(text(),'Confirmar')]"
        inputTienda = f"//strong[contains(.,'{tienda}')]"
        xpathfecha = "(//i[contains(@data-colindex,'1')])"
        xpathfecha2 = "(//i[contains(@data-colindex,'3')])"
        xpathfecha3 = "(//i[contains(@data-colindex,'5')])"
        ir_a_pago_xpath = "//button[contains(@class, 'shipping-step--finish')]"
        btnpay = "//*[@id='payment-data-submit']/span"
        self.web_driver.click(By.XPATH, btnAdress)
        self.web_driver.click(By.XPATH, inputAdress)
        self.web_driver.send_keys(By.XPATH, inputAdress, direccion)
        time.sleep(1)
        self.web_driver.click(By.XPATH, results)
        self.web_driver.click(By.XPATH, inputBcerrado)
        self.web_driver.click(By.XPATH, btnContinuar)
        self.web_driver.move(By.XPATH, inputTienda)
        self.web_driver.click(By.XPATH, inputTienda)
        try:
            self.web_driver.move(By.XPATH, xpathfecha)
            self.web_driver.click(By.XPATH, xpathfecha)
        except:
            try:
                self.web_driver.move(By.XPATH, xpathfecha2)
                self.web_driver.click(By.XPATH, xpathfecha2)
            except:
                self.web_driver.move(By.XPATH, xpathfecha3)
                self.web_driver.click(By.XPATH, xpathfecha3)
        time.sleep(1)
        self.web_driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);")
        self.web_driver.click(By.XPATH, ir_a_pago_xpath)
        self.web_driver.move(By.XPATH, btnpay)
        print('Script culminado con éxito')
        time.sleep(10)

    def envioClienteNuevo_DireccionElectro(self, direccion):
        btnAdress = "//button[contains(@id,'customButtonAddress')]"
        inputAdress = "//input[contains(@id,'autocomplete')]"
        results = "//div[@class='truncate'][contains(.,'Av. Lope de Vega 345, Ciudad Autónoma de Buenos Aires, Argentina')]"
        inputBcerrado = "//div//label[contains(text(), '¿Vivís en barrio cerrado?')]"
        btnContinuar = "//div[contains(text(),'Confirmar')]"
        close = "vtex__icon-close  "
        inputEnvio = "//strong[contains(text(), 'Envío a Domicilio en el día AMBA - Electro')]"
        inputEnvio2 = "//strong[contains(text(), 'Envío a Domicilio 24 Horas en Capital Federal y Gran Buenos Aires. - Electro')]"
        xpathfecha = "(//i[contains(@data-colindex,'1')])"
        xpathfecha2 = "(//i[contains(@data-colindex,'3')])"
        xpathfecha3 = "(//i[contains(@data-colindex,'5')])"
        ir_a_pago_xpath = "//button[contains(@class, 'shipping-step--finish')]"
        btnpay = "//*[@id='payment-data-submit']/span"
        self.web_driver.click(By.XPATH, btnAdress)
        self.web_driver.click(By.XPATH, inputAdress)
        self.web_driver.send_keys(By.XPATH, inputAdress, direccion)
        time.sleep(1)
        try:
            self.web_driver.click2(By.XPATH, results)
        except:
            self.web_driver.send_keys(By.XPATH, inputAdress, Keys.ARROW_DOWN)
            time.sleep(1)
            self.web_driver.send_keys(By.XPATH, inputAdress, Keys.ENTER)
        self.web_driver.click(By.XPATH, inputBcerrado)
        self.web_driver.click(By.XPATH, btnContinuar)
        time.sleep(6)
        self.web_driver.click(By.CLASS_NAME, close)
        try:
            self.web_driver.click(By.XPATH, inputEnvio)
        except:
            self.web_driver.click(By.XPATH, inputEnvio2)
        try:
            self.web_driver.move(By.XPATH, xpathfecha)
            self.web_driver.click(By.XPATH, xpathfecha)
        except:
            try:
                self.web_driver.move(By.XPATH, xpathfecha2)
                self.web_driver.click(By.XPATH, xpathfecha2)
            except:
                self.web_driver.move(By.XPATH, xpathfecha3)
                self.web_driver.click(By.XPATH, xpathfecha3)
        time.sleep(1)
        self.web_driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);")
        self.web_driver.click(By.XPATH, ir_a_pago_xpath)
        self.web_driver.move(By.XPATH, btnpay)
        print('Script culminado con éxito')
        time.sleep(10)

    def envio(self, direccion):
        direccion_xpath = "//input[@id='autocomplete']"
        select_suggestion_xpath = "//div[@id='results']"
        numero_xpath = "//input[@id='numero']"
        confirmar_xpath = "//div[contains(@class, 'buttonStyle')]"

        self.web_driver.send_keys(By.XPATH, direccion_xpath, direccion)
        self.web_driver.wait_appear(By.XPATH, select_suggestion_xpath)
        self.web_driver.click(By.XPATH, select_suggestion_xpath)
        self.web_driver.wait_appear(By.XPATH, numero_xpath)
        self.web_driver.send_keys(By.XPATH, numero_xpath, "1")
        self.web_driver.click(By.XPATH, confirmar_xpath)

        retiro_en_tienda_xpath = "//input[@id='Retiro en tienda']"
        primera_opcion_xpath = "//label[contains(@class, 'shipping-method--option')]/input"
        fecha_disponible_xpath = "//div[contains(@class, 'shipping-calendar__schedule-periods')]"
        self.web_driver.wait_appear(By.XPATH, retiro_en_tienda_xpath)
        self.web_driver.click(By.XPATH, retiro_en_tienda_xpath)
        self.web_driver.click(By.XPATH, primera_opcion_xpath)
        self.web_driver.click(By.XPATH, fecha_disponible_xpath)

        ir_a_pago_xpath = "//button[contains(@class, 'shipping-step--finish')]"
        self.web_driver.click(By.XPATH, ir_a_pago_xpath)

    def envioClienteRecurrente(self):
        envio_a_domicilio_xpath = "//label[contains(@class, 'shipping-method--option')]/input"
        fecha_disponible_xpath = "//div[contains(@class, 'shipping-calendar--iconDelivery')]"
        ir_a_pago_xpath = "//button[contains(@class, 'shipping-step--finish')]"
        self.web_driver.click(By.XPATH, envio_a_domicilio_xpath)
        self.web_driver.click(By.XPATH, fecha_disponible_xpath)
        self.web_driver.click(By.XPATH, ir_a_pago_xpath)


    def pay(self):
        giftcard = "//*[@id='payment-group-custom203PaymentGroupPaymentGroup']/span"
        self.web_driver.click(By.XPATH, giftcard)
        time.sleep(5)
        compra = "payment-submit-wrap"
        self.web_driver.click(By.CLASS_NAME, compra)

    def quit(self):
        self.web_driver.quit()
