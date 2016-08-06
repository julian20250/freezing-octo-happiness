/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package repaso;

import java.util.ArrayList;


/**
 *
 * @author julian
 */
public class Correlacion {
    
    public ArrayList<Estudiante> lista = new ArrayList<>();     

    static Estudiante Transform(String a){        
        String [] parts= a.split("-");
        Estudiante estudiante= new Estudiante(Integer.parseInt(parts[0]), 
            Float.parseFloat(parts[1]), Integer.parseInt(parts[2]),
            Integer.parseInt(parts[3]),Integer.parseInt(parts[4]),
            Integer.parseInt(parts[5]), Integer.parseInt(parts[6]));
        return estudiante;
    }
    
    public static float Correlation(float[] prom, int[] other){
        float correlation;
        float metamorfosis[] = new float[other.length];
        for (int x=0; x<other.length; x++) metamorfosis[x]=(float) other[x];
        correlation= Covarianza(prom, metamorfosis)/(Desviation(prom)*Desviation(metamorfosis));
        return correlation;
    }
    static float Mean(float[] list){
        float mean=0;
        for (int x=0; x<list.length; x++) mean+=list[x];
        mean= mean/list.length;
        return mean;
    }
    static float Covarianza(float[] a, float[] b){
        float mean1=Mean(a);
        float mean2=Mean(b);
        float covar = 0;
        for (int x =0; x<a.length; x++) covar+=(a[x]-mean1)*(b[x]-mean2);
        covar=covar/a.length;
        return covar;
    }
    
    static float Desviation(float[] a){
        float dev=0;
        float mean= Mean(a);
        for (int x=0; x<a.length; x++) dev +=Math.pow(a[x]-mean, 2);
        dev=dev/a.length;
        dev= (float) Math.pow(dev, 0.5);
        return dev;
    }
}
