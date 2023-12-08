import json
import os
import sys
def dict_to_txt(dictToPrint: dict,  save_path:str=None, file_prefix: str='', textbox: str=None):
        if save_path is None:
            save_path='./result/'
        if not os.path.isdir(save_path):
            os.makedirs(save_path)

        add_num =1
        save_path += f"/train_1_medic_accuracy"
        save_path_norepeat = save_path
        while os.path.isfile(f'{save_path_norepeat}.txt'):
            save_path_norepeat = save_path + f'_{add_num}'
            add_num +=1

        save_path_norepeat += '.txt'

        with open(save_path_norepeat, 'w', encoding='utf-8') as file:
            try:
                json.dump(dictToPrint, file, indent=2)
                
            except:
                print("cannot dump dictToPrint, use normal print")
                sys.stdout = file
                print(dictToPrint)
                sys.stdout = sys.__stdout__  # Reset stdout to default (console)
            try:
                if textbox is not None:
                    file.write('\n')
                    file.write(textbox)
                    file.write('\n')
            except:
                pass