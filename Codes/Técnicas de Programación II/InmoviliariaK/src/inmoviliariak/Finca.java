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
public class Finca extends ViviendaCasa{
    private int yearsConstruccion;
    public Finca(int id, int tipo, int metrosCuadrados, int estrato, int valorBaseMetroCuadrado, int numeroParqueaderos, boolean vigilanciaPrivada, String abstractData,
            int yearsConstruccion) {
        super(id, tipo, metrosCuadrados, estrato, valorBaseMetroCuadrado, numeroParqueaderos, vigilanciaPrivada, abstractData);
        this.yearsConstruccion=yearsConstruccion;
        this.setValue(this.getValue()-this.getOriginalValue()*.005*yearsConstruccion);
    }
    
}
