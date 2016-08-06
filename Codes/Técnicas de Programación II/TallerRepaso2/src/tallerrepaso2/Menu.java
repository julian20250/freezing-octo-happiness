/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package tallerrepaso2;

import java.util.Scanner;



/**
 *
 * @author Administrador
 */
public class Menu {
    public static void Desplegar(Scanner sc, TablaCifrado cifrado){
        
        String op;
        System.out.println("Tiene las siguientes opciones:");
        System.out.println("1. Agregar caracter de cifrado.");
        System.out.println("2. Verificar validez de la tabla.");
        System.out.println("3. Ver tabla de cifrado.");
        System.out.println("4. Reiniciar tabla.");
        System.out.println("5. Cifrar linea.");
        System.out.println("6. Descifrar linea.");
        System.out.println("7. Salir.\n");
        while (true){
            System.out.print("\nIngrese Opcion > ");
            op=sc.nextLine();

            switch (op) {
                case "1":
                    System.out.println("Ingrese los datos en el siguiente formato: (x-y)\n"+
                            "Si desea parar el ingreso de datos, digite break.");
                    String recibir="";
                    while (!recibir.equals("break")){
                        System.out.print("Ingrese el dato > ");
                        recibir = sc.nextLine();
                        if (!recibir.equals("break"))
                            cifrado.addCipher(recibir);
                    }
                    break;
                case "2":
                    System.out.println("La validez de su tabla es: "+cifrado.checkVality());
                    break;
                case "3":
                    System.out.println("Su tabla actual es la siguiente:");
                    for (int x=0; x<cifrado.datos.size(); x++)
                        System.out.println(cifrado.datos.get(x));
                    break;
                case "4":
                    System.out.print("Ingrese la palabra a encriptar > ");
                    String word=sc.nextLine();
                    System.out.println("La palabra codificada es: "+cifrado.cipherLine(word));
                    break;
                case "5":
                    System.out.print("Ingrese la palabra a desencriptar > ");
                    String word2=sc.nextLine();
                    System.out.println("La palabra descodificada es: "+cifrado.unCipherLine(word2));
                    break;
                case "6":
                    cifrado.Restart();
                    System.out.println("Tabla reiniciada.");
                    break;
                case "7":
                    System.exit(0);
                default:
                    System.out.println("Opcion no valida, intente de nuevo.");
                    break;
            }


        }
    }
    
}