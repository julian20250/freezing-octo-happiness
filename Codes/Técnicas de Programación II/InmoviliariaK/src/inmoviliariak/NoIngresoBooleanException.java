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
public class NoIngresoBooleanException extends Exception{
    public NoIngresoBooleanException(String message){
        super("Ingreso "+message+" en vez de true o false.");
    }
}
