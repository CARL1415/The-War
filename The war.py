print('''                                                     _..----.._                                   
                                                    ]_.--._____[                                  
                                                  ___|'--'__..|--._                               
                              __               """    ;            :                              
                            ()_ """"---...__.'""!":  /    ___       :                             
                               """---...__\]..__] | /    [ 0 ]      :                             
                                          """!--./ /      """        :                            
                                   __  ...._____;""'.__________..--..:_                           
                                  /  !"''''''!''''''''''|''''/' ' ' ' \"--..__  __..              
                                 /  /.--.    |          |  .'          \' ' '.""--.{'.            
             _...__            >=7 //.-.:    |          |.'             \ ._.__  ' '""'.          
          .-' /    """"----..../ "">==7-.....:______    |                \| |  "";.;-"> \         
          """";           __.."   .--"/"""""----...."""""----.....H_______\_!....'----""""]       
        _..---|._ __..--""       _!.-=_.            """""""""""""""                   ;"""        
       /   .-";-.'--...___     ." .-""; ';""-""-...^..__...-v.^___,  ,__v.__..--^"--""-v.^v,      
      ;   ;   |'.         """-/ ./;  ;   ;\P.        ;   ;        """"____;  ;.--""""// '""<,     
      ;   ;   | 1            ;  ;  '.: .'  ;<   ___.-'._.'------""""""____'..'.--""";;'  o ';     
      '.   \__:/__           ;  ;--""()_   ;'  /___ .-" ____---""""""" __.._ __._   '>.,  ,/;     
        \   \    /"""<--...__;  '_.-'/; ""; ;.'.'  "-..'    "-.      /"/    `__. '.   "---";      
         '.  'v ; ;     ;;    \  \ .'  \ ; ////    _.-" "-._   ;    : ;   .-'__ '. ;   .^".'      
           '.  '; '.   .'/     '. `-.__.' /;;;   .o__.---.__o. ;    : ;   '"";;""' ;v^" .^        
             '-. '-.___.'<__v.^,v'.  '-.-' ;|:   '    :      ` ;v^v^'.'.    .;'.__/_..-'          
                '-...__.___...---""'-.   '-'.;\     'WW\     .'_____..>."^"-""""""""    fsc       
                                      '--..__ '"._..'  '"-;;"""                                   
                                             """---'""""""                                        
  ''')
print("THE WAR")
print("Tu misión es escapar de la zona.")

print("Se escuchan disparos en la zona. Te encuentras en un callejon con 2 posibles salidas.")
salida = input("Elija entre la salida de la derecha o la de la izquierda: ")
if salida == "derecha":
    print("Puedes notar que este camino tiene salida.")
    print("Ahora haz llegado a una autopista.")
    accion = input("Decide entre esperar o cruzarla: ")
    if accion == "esperar":
        print("Decidiste esperar")
        print("Notaste que paso un soldado enemigo, te disparo, pero lograste huir. Ahora te encuentras herido!")
        auto = input("Encuentras autos decide cual auto eligir: el amarillo, el rojo, el azul o esperar ayuda: ")
        if auto == "rojo":
            print("El auto se encuentra descompuesto. Haz sido capturado!")
        elif auto == "azul":
            print("El auto azul tiene una llanta ponchada. Haz sido capturado!")
        elif auto == "amarillo":
            print("El auto amarillo tiene buen funcionamiento, haz logrado escapar de la zona. Haz ganado!")
        else:
            print("La ayuda no ha llegado a tiempo. Haz sido eliminado!")
    else:
        print("Estás cruzando la autopista, pero te encuentras a un soldado enemigo. Haz sido eliminado!") 
else:
    print("Te han encontrado!. Haz sido capturado.")
