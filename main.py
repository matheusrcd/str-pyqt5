import sys
from geradorWindows import *
from PyQt5.QtWidgets import QMainWindow, QApplication

def intimacao_comum_reclamante():
    all_var = {}
    all_var['nome'] = str(input('Nome do cliente: '))
    all_var['empresa'] = str(input('Nome da empresa: '))
    all_var['re_designada'] = str(input('Primeira designação?[s][n]: '))
    all_var['audiencia_tipo'] = str(input('Tipo da audiencia: '))
    all_var['data'] = str(input('Data: '))
    all_var['hora'] = str(input('Horário: '))
    all_var['vara'] = str(input('Vara: '))
    all_var['endereco'] = str(input('Endereço: '))
    all_var['conteudo'] = str(input('Corpo da intimação: '))
    all_var['advogado_infos'] = str(input('Advogado [Nome - Telefone]: '))

    txt = f"Prezado (a) Senhor(a) {all_var['nome']},\n\nNa sua audiência em face de {all_var['empresa']}, foi {all_var['re_designada']}:\nAudiência: {all_var['audiencia_tipo']}\nData: {all_var['data']}\nHora: {all_var['hora']}.\nVara: {all_var['vara']}\nLocal: {all_var['endereco']}\nA sua audiência {all_var['audiencia_tipo']} {all_var['conteudo']}. Em caso de dúvidas, entre em contato com a {all_var['advogado_infos']}.\n\nAtenciosamente,"
    return txt

def intimacao_comum_testemunha():
    all_var = {}
    all_var['nome'] = str(input('Nome do cliente: '))
    all_var['reclamante'] = str(input('Nome do reclamante: '))
    all_var['empresa'] = str(input('Nome da empresa: '))
    all_var['re_designada'] = str(input('Primeira designação?[s][n]: '))
    all_var['audiencia_tipo'] = str(input('Tipo da audiencia: '))
    all_var['data'] = str(input('Data: '))
    all_var['hora'] = str(input('Horário: '))
    all_var['vara'] = str(input('Vara: '))
    all_var['endereco'] = str(input('Endereço: '))
    all_var['conteudo'] = str(input('Corpo da intimação: '))
    all_var['advogado_infos'] = str(input('Advogado [Nome - Telefone]: '))

    txt = f"Prezado (a) Senhor(a) {all_var['nome']},\n\nReferente à ação trabalhista de {all_var['reclamante']}, em face de {all_var['empresa']}, a sua audiência foi {all_var['re_designada']}:\nAudiência: {all_var['audiencia_tipo']}\nData: {all_var['data']}\nHora: {all_var['hora']}.\nVara: {all_var['vara']}\nLocal: {all_var['endereco']}\nA sua audiência {all_var['audiencia_tipo']} {all_var['conteudo']}. Em caso de dúvidas, entre em contato com a {all_var['advogado_infos']}.\n\nAtenciosamente,"
    return txt


def intimacao_video_reclamante():
    all_var = {}
    all_var['nome'] = str(input('Nome do cliente: '))
    all_var['empresa'] = str(input('Nome da empresa: '))   
    all_var['reclamante'] = str(input('Nome do reclamante: '))
    all_var['re_designada'] = str(input('Primeira designação?[s][n]: '))
    all_var['audiencia_tipo'] = str(input('Tipo da audiencia: '))
    all_var['data'] = str(input('Data: '))
    all_var['hora'] = str(input('Horário: '))
    all_var['vara'] = str(input('Vara: '))
    all_var['link'] = str(input('Link: '))
    all_var['codigo'] = str(input('Codigo de acesso: '))
    all_var['senha'] = str(input('Senha de acesso: '))
    all_var['conteudo'] = str(input('Corpo da intimação: '))
    all_var['advogado_infos'] = str(input('Advogado [Nome - Telefone]: '))

    txt = f"Prezado (a) Senhor(a) {all_var['nome']},\n\nNa sua audiência em face de {all_var['empresa']}, foi {all_var['re_designada']}:\nAudiência: {all_var['audiencia_tipo']}\nData: {all_var['data']}]\nHora: {all_var['hora']}\nVara: {all_var['vara']}\nLocal: A audiência será realizada pela Plataforma Emergencial de Videoconferência [Zoom/Google Meet]. (obs para Matheus Ricardo: se for Meet, não tem cód. De acesso nem senha, só link)\nLink:{all_var['link']}\nCódigo de acesso: {all_var['codigo']}\nSenha: {all_var['senha']}\n\nA sua audiência {all_var['audiencia_tipo']} {all_var['conteudo']}. Em caso de dúvidas, entre em contato com a {all_var['advogado_infos']}.\n\nAtenciosamente,"
    return txt

def intimacao_video_testemunha():
    all_var = {}
    all_var['nome'] = str(input('Nome do cliente: '))   
    all_var['reclamante'] = str(input('Nome do reclamante: '))
    all_var['empresa'] = str(input('Nome da empresa: '))
    all_var['re_designada'] = str(input('Primeira designação?[s][n]: '))
    all_var['audiencia_tipo'] = str(input('Tipo da audiencia: '))
    all_var['data'] = str(input('Data: '))
    all_var['hora'] = str(input('Horário: '))
    all_var['vara'] = str(input('Vara: '))
    all_var['link'] = str(input('Link: '))
    all_var['codigo'] = str(input('Codigo de acesso: '))
    all_var['senha'] = str(input('Senha de acesso: '))
    all_var['conteudo'] = str(input('Corpo da intimação: '))
    all_var['advogado_infos'] = str(input('Advogado [Nome - Telefone]: '))

    txt = f"Prezado (a) Senhor(a) {all_var['nome']},\n\nReferente à ação trabalhista de {all_var['reclamante']}, em face de {all_var['empresa']}, a sua audiência foi {all_var['re_designada']}:\nAudiência:{all_var['audiencia_tipo']}\nData: {all_var['data']}\nHora: {all_var['hora']}\nVara: {all_var['vara']}\nLocal: A audiência será realizada pela Plataforma Emergencial de Videoconferência [Zoom/Google Meet]. (obs para Matheus Ricardo: se for Meet, não tem cód. De acesso nem senha, só link\nLink:{all_var['link']}\nCódigo de acesso: {all_var['codigo']}\nSenha: {all_var['senha']} \n\nA sua audiência {all_var['audiencia_tipo']} {all_var['conteudo']}. Em caso de dúvidas, entre em contato com a {all_var['advogado_infos']}.\n\nAtenciosamente,"
    return txt


class MainWindow(QMainWindow, Ui_WindowComumReclamante):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        self.botaoGerar.clicked.connect(self.intimacao_comum_reclamante)
        self.botaoGerar_2.clicked.connect(self.intimacao_comum_testemunha)
        self.botaoGerar_4.clicked.connect(self.intimacao_video_reclamante)
        self.botaoGerar_5.clicked.connect(self.intimacao_video_testemunha)
        

    def intimacao_comum_reclamante(self):
        all_var = {}
        all_var['nome'] = self.inputNome.text()
        all_var['empresa'] = self.inputEmpresa.text()
        if self.checkBox.isChecked():
            all_var['re_designada'] = 'redesignada'
        else:
            all_var['re_designada'] = 'designada'
        all_var['audiencia_tipo'] = self.inputAudiencia.text()
        all_var['data'] = str(self.inputData.text())
        all_var['hora'] = str(self.inputHora.text())
        all_var['vara'] = self.inputVara.text()
        all_var['endereco'] = self.inputEndereco.text()
        all_var['conteudo'] = self.inputConteudo.text()
        all_var['advogado_infos'] = self.inputAdvogado.text()
    
        txt = f"Prezado (a) Senhor(a) {all_var['nome']},\n\nNa sua audiência em face de {all_var['empresa']}, foi {all_var['re_designada']}:\nAudiência: {all_var['audiencia_tipo']}\nData: {all_var['data']}\nHora: {all_var['hora']}.\nVara: {all_var['vara']}\nLocal: {all_var['endereco']}\nA sua audiência {all_var['audiencia_tipo']} {all_var['conteudo']}. Em caso de dúvidas, entre em contato com a {all_var['advogado_infos']}.\n\nAtenciosamente,"
        self.textoFinal.setText(txt)

    def intimacao_comum_testemunha(self):
        all_var = {}
        all_var['nome'] = self.inputNome_2.text()
        all_var['reclamante'] = self.inputReclamante.text()
        all_var['empresa'] = self.inputEmpresa_2.text()
        if self.checkBox_2.isChecked():
            all_var['re_designada'] = 'redesignada'
        else:
            all_var['re_designada'] = 'designada'
        all_var['audiencia_tipo'] = self.inputAudiencia_2.text()
        all_var['data'] = str(self.inputData_2.text())
        all_var['hora'] = str(self.inputHora_2.text())
        all_var['vara'] = self.inputVara_2.text()
        all_var['endereco'] = self.inputEndereco_2.text()
        all_var['conteudo'] = self.inputConteudo_2.text()
        all_var['advogado_infos'] = self.inputAdvogado_2.text()
    
        txt = f"Prezado (a) Senhor(a) {all_var['nome']},\n\nReferente à ação trabalhista de {all_var['reclamante']}, em face de {all_var['empresa']}, a sua audiência foi {all_var['re_designada']}:\nAudiência: {all_var['audiencia_tipo']}\nData: {all_var['data']}\nHora: {all_var['hora']}.\nVara: {all_var['vara']}\nLocal: {all_var['endereco']}\nA sua audiência {all_var['audiencia_tipo']} {all_var['conteudo']}. Em caso de dúvidas, entre em contato com a {all_var['advogado_infos']}.\n\nAtenciosamente,"
        self.textoFinal_2.setText(txt)

    def intimacao_video_reclamante(self):
        all_var = {}
        all_var['nome'] = self.inputNome_4.text()
        all_var['reclamante'] = self.inputReclamante_3.text()
        all_var['empresa'] = self.inputEmpresa_4.text()
        if self.checkBox_4.isChecked():
            all_var['re_designada'] = 'redesignada'
        else:
            all_var['re_designada'] = 'designada'
        all_var['audiencia_tipo'] = self.inputAudiencia_4.text()
        all_var['data'] = str(self.inputData_4.text())
        all_var['hora'] = str(self.inputHora_4.text())
        all_var['vara'] = self.inputVara_4.text()
        all_var['link'] = self.inputLink.text()
        all_var['codigo'] = self.inputCodigo.text()
        all_var['senha'] = self.inputSenha.text()
        all_var['conteudo'] = self.inputConteudo_4.text()
        all_var['advogado_infos'] = self.inputAdvogado_4.text()

        if self.meet.isChecked():
            txt = f"Prezado (a) Senhor(a) {all_var['nome']},\n\nNa sua audiência em face de {all_var['empresa']}, foi {all_var['re_designada']}:\nAudiência: {all_var['audiencia_tipo']}\nData: {all_var['data']}\nHora: {all_var['hora']}\nVara: {all_var['vara']}\nLocal: A audiência será realizada pela Plataforma Emergencial de Videoconferência Google Meet.\nLink:{all_var['link']}\n\nA sua audiência {all_var['audiencia_tipo']} {all_var['conteudo']}. Em caso de dúvidas, entre em contato com a {all_var['advogado_infos']}.\n\nAtenciosamente,"
            self.textoFinal_4.setText(txt)
        else:
            txt = f"Prezado (a) Senhor(a) {all_var['nome']},\n\nNa sua audiência em face de {all_var['empresa']}, foi {all_var['re_designada']}:\nAudiência: {all_var['audiencia_tipo']}\nData: {all_var['data']}\nHora: {all_var['hora']}\nVara: {all_var['vara']}\nLocal: A audiência será realizada pela Plataforma Emergencial de Videoconferência Zoom.\nLink:{all_var['link']}\nCódigo de acesso: {all_var['codigo']}\nSenha: {all_var['senha']}\n\nA sua audiência {all_var['audiencia_tipo']} {all_var['conteudo']}. Em caso de dúvidas, entre em contato com a {all_var['advogado_infos']}.\n\nAtenciosamente,"
            self.textoFinal_4.setText(txt)

    def intimacao_video_testemunha(self):
        all_var = {}
        all_var['nome'] = self.inputNome_5.text()
        all_var['reclamante'] = self.inputReclamante_4.text()
        all_var['empresa'] = self.inputEmpresa_5.text()
        if self.checkBox_5.isChecked():
            all_var['re_designada'] = 'redesignada'
        else:
            all_var['re_designada'] = 'designada'
        all_var['audiencia_tipo'] = self.inputAudiencia_5.text()
        all_var['data'] = str(self.inputData_5.text())
        all_var['hora'] = str(self.inputHora_5.text())
        all_var['vara'] = self.inputVara_5.text()
        all_var['link'] = self.inputLink_2.text()
        all_var['codigo'] = self.inputCodigo_2.text()
        all_var['senha'] = self.inputSenha_2.text()
        all_var['conteudo'] = self.inputConteudo_5.text()
        all_var['advogado_infos'] = self.inputAdvogado_5.text()

        if self.meet_2.isChecked():
            txt = f"Prezado (a) Senhor(a) {all_var['nome']},\n\nReferente à ação trabalhista de {all_var['reclamante']}, em face de {all_var['empresa']}, a sua audiência foi {all_var['re_designada']}:\nAudiência:{all_var['audiencia_tipo']}\nData: {all_var['data']}\nHora: {all_var['hora']}\nVara: {all_var['vara']}\nLocal: A audiência será realizada pela Plataforma Emergencial de Videoconferência Google Meet. \nLink:{all_var['link']}\n\nA sua audiência {all_var['audiencia_tipo']} {all_var['conteudo']}. Em caso de dúvidas, entre em contato com a {all_var['advogado_infos']}.\n\nAtenciosamente,"
            self.textoFinal_5.setText(txt)
        else:
            txt = f"Prezado (a) Senhor(a) {all_var['nome']},\n\nReferente à ação trabalhista de {all_var['reclamante']}, em face de {all_var['empresa']}, a sua audiência foi {all_var['re_designada']}:\nAudiência:{all_var['audiencia_tipo']}\nData: {all_var['data']}\nHora: {all_var['hora']}\nVara: {all_var['vara']}\nLocal: A audiência será realizada pela Plataforma Emergencial de Videoconferência Zoom. \nLink:{all_var['link']}\nCódigo de acesso: {all_var['codigo']}\nSenha: {all_var['senha']} \n\nA sua audiência {all_var['audiencia_tipo']} {all_var['conteudo']}. Em caso de dúvidas, entre em contato com a {all_var['advogado_infos']}.\n\nAtenciosamente,"
            self.textoFinal_5.setText(txt)




if __name__ == '__main__':
    qt = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    qt.exec_()