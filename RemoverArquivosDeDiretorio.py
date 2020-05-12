import os
from abc import ABC, abstractmethod

class RemoverFile:
    
    @abstractmethod
    def removerArqDiretorioEhSubDiretorio(diretorio_remocao, remocao):

        lista_remocao = ['implements', 'Track3D', 'Materials', 'CoverageHistory', 'LineFeature', 'Swaths', 'EventHistory', 'newField', 'origin', 'EventSummary']
       
        lista_remocao.append(remocao)        

        from datetime import datetime
        data_e_hora_atuais = datetime.now()
        formato_data_e_hora = '%d/%m/%Y %H:%M:%S'
        time_inicio = data_e_hora_atuais.strftime(formato_data_e_hora)
        print("Remoção de arquivos iniciada..... às: {0}".format(time_inicio))
        
        diretorio = os.listdir(diretorio_remocao)
        registros_excluidos = 0
        for pasta in diretorio:
            diretorio_atual = diretorio_remocao + "\\" + pasta
            for root, dirs, files in os.walk(diretorio_atual):
                for file in files:
                    for list in lista_remocao:
                        if file.startswith(str(list)) or file.endswith('.pos'):
                            try:
                                print("Arquivo removido....: {0}".format(file))                                
                                registros_excluidos = registros_excluidos + 1
                                os.remove(os.path.join(root, file))
                            except:
                                print("Ops.... Erro ao remover o arquivo:".format(file))
                        else:                            
                            pass
        data_e_hora_atuais = datetime.now()
        time_termino = data_e_hora_atuais.strftime(formato_data_e_hora)
        time_total = datetime.strptime(time_termino, formato_data_e_hora) - datetime.strptime(time_inicio, formato_data_e_hora)
        print("Processo iniciado às: {0}, finalizado às: {1}".format(time_inicio, time_termino))
        print("Total de arquivos excluídos: {0}, Tempo gasto: {1}".format(registros_excluidos, time_total)) 
