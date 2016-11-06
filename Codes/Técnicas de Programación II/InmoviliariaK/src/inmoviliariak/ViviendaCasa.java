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
public class ViviendaCasa extends Inmueble{
    private int numeroParqueaderos;
    private boolean vigilanciaPrivada;
    public ViviendaCasa(int id, int tipo, int metrosCuadrados, int estrato,
            int valorBaseMetroCuadrado, int numeroParqueaderos, boolean
                    vigilanciaPrivada, String abstractData) {
        super(id, tipo, metrosCuadrados, estrato, valorBaseMetroCuadrado,
                abstractData);
        this.numeroParqueaderos=numeroParqueaderos;
        this.vigilanciaPrivada=vigilanciaPrivada;
        this.setValue(this.getOriginalValue()+this.getOriginalValue()*.025*estrato);
        if (!vigilanciaPrivada)
            this.setValue(this.getValue()-.1*this.getOriginalValue());
    }

    public int getNumeroParqueaderos() {
        return numeroParqueaderos;
    }
    
    
}
