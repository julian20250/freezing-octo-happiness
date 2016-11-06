/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package inmoviliariak;

/**
 *
 * @author Ingenierias
 */
public class IdentificadorRepetidoException extends Exception {
    public IdentificadorRepetidoException(String message) { 
        super("El identificador "+message+" ya se encuentra en la lista."); 
    }   
}
