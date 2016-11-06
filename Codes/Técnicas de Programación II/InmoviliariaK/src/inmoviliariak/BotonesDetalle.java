/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package inmoviliariak;

import java.awt.GridLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import javax.swing.ImageIcon;
import javax.swing.JButton;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.JTextField;

/**
 *
 * @author julian
 */
class BotonesDetalle extends JPanel implements ActionListener{
    int i=0;
    MenuInmoviliariaK menu;
    JTextField[] campos;
    JLabel imageLabel;
    ImageIcon[] photos;
    public BotonesDetalle(JTextField[] campos, MenuInmoviliariaK menu, JLabel imageLabel,
            ImageIcon[] photos){
        this.menu=menu;
        this.imageLabel=imageLabel;
        this.campos=campos;
        this.photos=photos;
        setLayout(new GridLayout(1, 2));
        JButton anterior = new JButton("Anterior");
        anterior.addActionListener(this);
        anterior.setActionCommand("anterior");
        JButton siguiente = new JButton("Siguiente");
        siguiente.addActionListener(this);
        siguiente.setActionCommand("siguiente");
        add(anterior); add(siguiente);
    }

    @Override
    public void actionPerformed(ActionEvent e) {
        if (menu.l.size()!=0){
            if (e.getActionCommand().equals("anterior")){            
                i--;
                if (i<=-1)
                    i=menu.l.size()-1;
            }else if(e.getActionCommand().equals("siguiente")){
                i++;
                if (i>=menu.l.size())
                    i=0;
            }
            String data= menu.l.get(i).toString();
            String[] spl= data.split("-");
            campos[0].setText(spl[0]);
            campos[1].setText(spl[1]);
            campos[2].setText(spl[2]);
            campos[3].setText(spl[3]);
            campos[4].setText(spl[4]);
            switch (spl[1]){
                case "1": 
                    imageLabel.setIcon(photos[1]);
                    campos[5].setText(spl[5]);
                    campos[6].setText(null);
                    campos[7].setText(null);
                    campos[8].setText(null);

                    break;

                case "2":
                    imageLabel.setIcon(photos[2]);
                    campos[5].setText(null);
                    campos[6].setText(spl[5]);
                    campos[7].setText(spl[6]);
                    campos[8].setText(null);
                    break;

                case "3":
                    imageLabel.setIcon(photos[3]);
                    campos[5].setText(null);
                    campos[6].setText(spl[5]);
                    campos[7].setText(null);
                    campos[8].setText(spl[6]);
                    break;
            }
        }
    }
}
