/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package inmoviliariak;

/**
 *
 * @author julian
 */
public class NumeroInadecuadoDeParametrosException extends Exception {
    public NumeroInadecuadoDeParametrosException(int message1, int message2) { 
        super("Hay que ingresar "+message1+" parametros, usted ingreso "+message2); 
    }   
}
