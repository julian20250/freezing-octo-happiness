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
public class ViviendaApartamento extends Inmueble{
    private int numeroParqueaderos;
    private int piso;
    public ViviendaApartamento(int id, int tipo, int metrosCuadrados, int estrato,
            int valorBaseMetroCuadrado, int numeroParqueaderos, int piso,
            String abstractData) {
        super(id, tipo, metrosCuadrados, estrato, valorBaseMetroCuadrado,
                abstractData);
        this.numeroParqueaderos=numeroParqueaderos;
        this.piso=piso;        
        this.setValue(this.getOriginalValue()+this.getOriginalValue()*.025*estrato
                -this.getOriginalValue()*0.015*piso);
        
    }
    
    
}
