import java.awt.event.*;  
import javax.swing.*;    
public class Main {  
  public static void welcome(String password) {
    JLabel welcome=new JLabel();
    welcome.setText("Welcome you and password is " + password);
  }
  public static void main(String[] args) {  
    JFrame f=new JFrame("InStudio JavaC");  
    final JLabel tf=new JLabel();  
    tf.setText("Get Started!");
    tf.setBounds(50,50, 150,20);  
    JButton b=new JButton("Click Here");  
    b.setBounds(50,100,95,30);  
    b.addActionListener(new ActionListener(){  
  public void actionPerformed(ActionEvent e){  
            tf.setText("Welcome to InfinityX.");  
            welcome("InfinityX");
        }  
    });  
    f.add(b);f.add(tf);  
    f.setSize(400,400);  
    f.setLayout(null);  
    f.setVisible(true);   
  }
}
