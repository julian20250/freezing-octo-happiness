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
public class Inmueble {
    private int id;
    private String abstractData;
    private int tipo;
    private int metrosCuadrados;
    private int estrato;
    private double originalValue;
    private double value;
    private double tax;
    private int valorBaseMetroCuadrado;
    public Inmueble(int id, int tipo, int metrosCuadrados, int estrato,
            int valorBaseMetroCuadrado, String abstractData){
        this.id=id;
        this.tipo=tipo;
        this.metrosCuadrados=metrosCuadrados;
        this.abstractData=abstractData;
        this.estrato=estrato;
        this.valorBaseMetroCuadrado=valorBaseMetroCuadrado;
        this.originalValue=metrosCuadrados*valorBaseMetroCuadrado;
        if (tipo==2 || tipo==3)
            this.tax=this.originalValue*.05;
        else{
            if(metrosCuadrados>100)
                this.tax=this.originalValue*.07;
            else
                this.tax=0;
        }
    }

    @Override
    public String toString() {
        return abstractData;
    }

    public double getOriginalValue() {
        return originalValue;
    }

    public int getId() {
        return id;
    }

    public double getValue() {
        return value;
    }

    public void setValue(double value) {
        this.value = value;
    }

    public double getTax() {
        return tax;
    }

    public int getEstrato() {
        return estrato;
    }

    public int getTipo() {
        return tipo;
    }
    
    
    
}
