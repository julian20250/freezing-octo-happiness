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
public class Oficina extends Inmueble{
    private boolean parqueaderoVisitante;
    public Oficina(int id, int tipo, int metrosCuadrados, int estrato,
            int valorBaseMetroCuadrado, boolean parqueaderoVisitante,
            String abstractData){
        super(id, tipo, metrosCuadrados, estrato, valorBaseMetroCuadrado,
                abstractData);
        this.parqueaderoVisitante=parqueaderoVisitante;
        this.setValue(this.getOriginalValue()+this.getOriginalValue()*.05*estrato);
        if (parqueaderoVisitante)
            this.setValue(this.getValue()+.2*this.getOriginalValue());
        else
            this.setValue(this.getValue()-.1*this.getOriginalValue());
    }
}
