//Username :- admin & Password :- admin 
import java.awt.Font;
import java.awt.HeadlessException;
import javax.swing.*;
import java.awt.event.*;
import java.sql.*;
import java.util.Random;
public class atm extends JFrame implements ActionListener
{ 
    //Main Frame
    JFrame main;
    JLabel lo,pa,lae;
    JTextField lt1,pt2;
    JButton lb,cl;
    //End
    
    //For Sub-Main
    JLabel la;
    JFrame submain;
    JButton b,b1,b2,b3,b4,b5,b6;
    //End
    
    //For Pin generation
    JLabel l,l1,l2;
    JTextField t;
    JFrame f;
    JButton confirm,close;
    //End    
    
    //FOR BALANCE ENQUIRY
    JFrame f1;
    JLabel bal,rs,ac;
    JTextField ac1;
    JButton balclose,enq;
    //End
    
    //CONTACT US 
    JFrame f2;
    JLabel about;
    JButton abclose;
    //End
    
    //QUICK CASH
    JFrame f3;
    JLabel r,r2,r3,r4,lca,label;
    JTextField tf1,tf3,tf4,tf5,tca;
    JButton ok,caclose;
    //End
    
    //CASH WITHDRAWAL
    JFrame f4;
    JLabel c1,c2;
    JTextField j,j1;
    JButton ok1,close1;
    //End
    
    //PIN CHANGE
    JFrame f5;
    JLabel in,no,pin;
    JTextField pe,pie;
    JButton con,pclose,pop;
    //End
    
    public atm()
    {
        //MAIN FRAME STARTS
        main = new JFrame(" WELCOME TO ATM ");
        lo = new JLabel(" Username : ");
        pa = new JLabel(" Password : ");
        lt1 = new JTextField(10);
        pt2 = new JTextField(10);
        lb = new JButton(" LOGIN ");
        cl = new JButton(" CLOSE ");
        lb.addActionListener(this);
        cl.addActionListener(this);
        lo.setBounds(100,150,150,30);
        pa.setBounds(100,200,150,30);
        lt1.setBounds(180,150,150,30);
        pt2.setBounds(180,200,150,30);
        lb.setBounds(130,250,100,30);
        cl.setBounds(250,250,100,30);
        main.add(lo);
        main.add(lt1);
        main.add(pa);
        main.add(pt2);
        main.add(lb);
        main.add(cl);
        main.setLayout(null);
        main.setSize(700,500);
        main.setVisible(true);
        //MAIN FRAME ENDS
        
        //SUB-MAIN FRAME STARTS
        submain=new JFrame(" ATM ");
        b=new JButton(" PIN CHANGE ");
        b1=new JButton(" PIN GENERATION ");
        b2=new JButton(" CONTACT US ");
        b3=new JButton(" BALANCE ENQUIRY ");
        b4=new JButton("CASH WITHDRAWAL");
        b5=new JButton(" QUICK CASH ");
        b6=new JButton(" CLOSE ");
        la=new JLabel(" WELCOME TO ATM ");
        la.setFont(new Font("Comic Sans MS",Font.PLAIN,48));
        b.setBounds(10,150,150,30);
        b1.setBounds(10,250,150,30);
        b2.setBounds(10,350,150,30);
        b3.setBounds(500,150,150,30);
        b4.setBounds(500,250,150,30);
        b5.setBounds(500,350,150,30);
        b6.setBounds(270,400,100,30);
        la.setBounds(70,20,500,50);
        b.addActionListener(this);
        b1.addActionListener(this);
        b2.addActionListener(this);
        b3.addActionListener(this);
        b4.addActionListener(this);
        b5.addActionListener(this);
        b6.addActionListener(this);
        submain.add(b);submain.add(b1);
        submain.add(b2);submain.add(b3);
        submain.add(b4);submain.add(b5);
        submain.add(b6);submain.add(la);
        submain.setLayout(null);
        submain.setSize(700,500);
        submain.setVisible(false);
        //SUB-MAIN FRAME ENDS
        
        //PIN GENERATION FRAME
        f=new JFrame(" PIN GENERATION ");
        l=new JLabel(" ACCOUNT NO :- ");
        t=new JTextField(10);
        l1 = new JLabel(" YOUR PIN IS :- ");
        l2 = new JLabel(" ");
        confirm=new JButton(" CONFIRM ");
        close=new JButton(" CLOSE ");
        confirm.addActionListener(this);
        close.addActionListener(this);
        l.setBounds(100,100,250,30);
        t.setBounds(200,100,100,30);
        l1.setBounds(100,150,100,30);
        l2.setBounds(200,150,100,30);
        confirm.setBounds(100,190,100,30);
        close.setBounds(220,190,100,30);
        f.add(l);f.add(t);f.add(l1);f.add(l2);
        f.add(confirm);f.add(close);
        f.setLayout(null);
        f.setSize(650,400);
        //END
        
        //BALANCE ENQUIRY FRAME STARTS
        f1=new JFrame(" BALANCE ENQUIRY ");
        bal=new JLabel(" YOUR BALANCE IS : ");
        rs=new JLabel(" ");
        ac=new JLabel(" ACCOUNT NO : ");
        ac1=new JTextField(10);
        balclose=new JButton(" CLOSE ");
        enq=new JButton(" ENQUIRE ");
        bal.setBounds(130,140,150,30);
        rs.setBounds(260,140,100,30);
        ac.setBounds(130,80,150,30);
        ac1.setBounds(230,80,120,30);
        balclose.setBounds(280,200,100,30);
        enq.setBounds(150,200,100,30);
        balclose.addActionListener(this);
        enq.addActionListener(this);
        f1.add(ac);f1.add(ac1);f1.add(bal);
        f1.add(rs);f1.add(enq);f1.add(balclose);
        f1.setLayout(null);
        f1.setSize(650,400);
        //END
        
        //CONTACT US FRAME STARTS
        f2=new JFrame(" CONTACT US ");
        about=new JLabel("<html>Call us : " + " Toll free number : 1800 11 2211 , " + " Toll free number : 1800 425 3800 " +
                         "<br>Toll free number : 080-26599990" + "<br>"+"<br>" + "Text us : " + "<br>Unhappy with services : SMS UNHAPPY to 8008 20 20 20" +
                         "<br>"+"<br> Missed call Banking @ SBI QUICK " + "<br>"+"<br>" + " Write to us  : " + "<br>Customer Service Department" +
                         "<br>State Bank of India" + "<br>State Bank Bhavan, 16th Floor" + "<br>Madam Cama Road," + "<br>Mumbai 400 021." +"<br>" +                         
                         "<br> Tel : 022-22029456. " + "<br> Fax : 022 22742431. " + "<br>");
        abclose=new JButton(" CLOSE ");
        about.setBounds(80,-350,1000,1000);
        abclose.setBounds(200,330,100,30);
        abclose.addActionListener(this);
        f2.add(about);
        f2.add(abclose);
        f2.setLayout(null);
        f2.setSize(650,400);
        //END
        
        //QUICK CASH FRAME STARTS
        f3=new JFrame(" QUICK CASH ");
        label=new JLabel(" ** ENTER ONLY NUMBER OF NOTES ");
        r=new JLabel(" X 2000 ");
        r2=new JLabel(" X 500 ");
        r3=new JLabel(" X 200 ");
        r4=new JLabel(" X 100 ");
        lca=new JLabel("ACCOUNT NO :- ");
        tf1=new JTextField(4);
        tf3=new JTextField(4);
        tf4=new JTextField(4);
        tf5=new JTextField(4);
        tca= new JTextField(10);
        ok=new JButton(" OK ");
        caclose=new JButton(" CLOSE ");
        ok.addActionListener(this);
        caclose.addActionListener(this);
        label.setBounds(40,10,250,30);
        lca.setBounds(50,50,150,30);
        tca.setBounds(160,50,100,30);
        r.setBounds(300,100,100,30);
        r2.setBounds(300,150,100,30);
        r3.setBounds(300,200,100,30);
        r4.setBounds(300,250,100,30);
        tf1.setBounds(235,105,50,20);
        tf3.setBounds(235,155,50,20);
        tf4.setBounds(235,205,50,20);
        tf5.setBounds(235,255,50,20);
        ok.setBounds(160,300,100,30);
        caclose.setBounds(320,300,100,30);
        f3.add(label);f3.add(lca);f3.add(tca);
        f3.add(r);f3.add(r2);f3.add(r3);f3.add(r4);
        f3.add(tf1);f3.add(tf3);f3.add(tf4);f3.add(tf5);
        f3.add(ok);f3.add(caclose);
        f3.setLayout(null);
        f3.setSize(600,500);
        //END
        
        //CASH WITHDRAWAL FRAME
        f4=new JFrame(" CASH WITHDRAWAL ");
        c1=new JLabel(" ENTER THE AMOUNT : ");
        j=new JTextField(10);
        c2= new JLabel(" ACCOUNT NO : ");
        j1=new JTextField(10);
        ok1=new JButton(" CONFIRM ");
        close1=new JButton(" CLOSE ");
        close1.addActionListener(this);
        ok1.addActionListener(this);
        c1.setBounds(100,70,150,30);
        j.setBounds(230,70,100,30);
        c2.setBounds(100,30,150,30);
        j1.setBounds(230,30,100,30);
        ok1.setBounds(100,130,100,30);
        close1.setBounds(230,130,100,30);
        f4.add(c2);f4.add(j1);
        f4.add(c1);f4.add(j);
        f4.add(ok1);f4.add(close1);
        f4.setLayout(null);
        f4.setSize(600,350);
        //End
        
        //PIN CHANGE FRAME
        f5=new JFrame(" PIN CHANGE ");
        in=new JLabel(" ACCOUNT NO : ");
        pe=new JTextField(10);
        pin = new JLabel("ENTER NEW PIN : ");
        pie = new JTextField(4);
        con=new JButton(" CONFIRM ");
        pclose=new JButton(" CLOSE ");
        in.setBounds(220,100,250,30);
        pe.setBounds(320,100,100,30);
        con.setBounds(220,190,100,30);
        pclose.setBounds(350,190,100,30);
        pin.setBounds(210,145,250,30);
        pie.setBounds(320,150,100,30);
        con.addActionListener(this);
        pclose.addActionListener(this);
        f5.add(in);
        f5.add(pe);
        f5.add(con);f5.add(pclose);
        f5.add(pin);f5.add(pie);
        f5.setLayout(null);
        f5.setSize(650,400);
        //End
    }

    @Override
    public void actionPerformed(ActionEvent e) 
    {
        if(e.getSource()==b1)
        {
            submain.setVisible(false);
            f.setVisible(true);
        }
        if(e.getSource()==close)
        {
            f.setVisible(false);
            submain.setVisible(true);
            t.setText("");
            l2.setText("");
            
        }
        if(e.getSource()==b3)
        {
            submain.setVisible(false);
            f1.setVisible(true);
        }
        if(e.getSource()==balclose)
        {
            f1.setVisible(false);
            submain.setVisible(true);
            rs.setText("");
            ac1.setText("");
        }
        if(e.getSource()==b2)
        {
            f2.setVisible(true);
            submain.setVisible(false);
        }
        if(e.getSource()==abclose)
        {
            f2.setVisible(false);
            submain.setVisible(true);
        }
        if(e.getSource()==b5)
        {
            f3.setVisible(true);
            submain.setVisible(false);
        }
        if(e.getSource()==caclose)
        {
            f3.setVisible(false);
            submain.setVisible(true);
            tf1.setText("");
            tf3.setText("");
            tf4.setText("");
            tf5.setText("");
            tca.setText("");
        }
        if(e.getSource()==b4)
        {
            f4.setVisible(true);
            submain.setVisible(false);
        }
        if(e.getSource()==close1)
        {
            submain.setVisible(true);
            f4.setVisible(false);
            j.setText("");
            j1.setText("");
        }
        if(e.getSource()==b)
        {
            submain.setVisible(false);
            f5.setVisible(true);
        }
        if(e.getSource()==pclose)
        {
            submain.setVisible(true);
            f5.setVisible(false);
            pe.setText("");
            pie.setText("");
        }
        if(e.getSource()==b6)
        {
            submain.setVisible(false);
            System.exit(0);
        }
        if(e.getSource()==cl)
        {
            main.setVisible(false);
            System.exit(0);
        }
        if (e.getSource()== lb)
        {   	
            String s=lt1.getText();
            String a=pt2.getText();
            if(s.equals("admin") && a.equals("admin"))
            {
                main.setVisible(false);
                submain.setVisible(true);
            }
        }
        /*if(e.getSource()==with)
        {
            int a = tca.getText().length();
            if(a == 10)
            {
                 f6.setVisible(false);
                 f3.setVisible(true);
                 tca.setText("");
            }
            else
            {
                JOptionPane.showMessageDialog(null,"Enter Valid Account No");
            }
        }*/
        if(e.getSource()== ok1)
        {
            int a = j1.getText().length();
            int b = Integer.parseInt(j.getText());
            if(a == 10 && b > 100)
            {
            try
            {
                Class.forName("com.mysql.jdbc.Driver");
                Connection conn =DriverManager.getConnection("jdbc:mysql://localhost:33060/atm","root","sagar");
                String sql="update atm set cash = cash - ? where account_no = ?";
                PreparedStatement pstmt = conn.prepareStatement(sql);
                int r11 = Integer.parseInt(j.getText());
                pstmt.setString(1,j.getText());
                pstmt.setString(2,j1.getText());
                JOptionPane.showMessageDialog(null,"Take Your Cash :-  " + r11 + " Rs");
                pstmt.executeUpdate();
                pstmt.close();
            }
            catch(ClassNotFoundException | SQLException | HeadlessException | NumberFormatException ex)
            {
                String msg = "ACCOUNT DOESN'T HAVE SUFFICIENT BALANCE";
                String title = "ERROR"; 
                System.out.println("sql Error");
                int type = JOptionPane.ERROR_MESSAGE;
                JOptionPane.showMessageDialog(null,msg,title,type);
            }}
            else if(a == 10 && b < 100)
            {
                JOptionPane.showMessageDialog(this,"Amount Entered Should Be Greater Than 100");         
            }
            else
            {
                JOptionPane.showMessageDialog(this,"Amount Entered Should Be Greater Than 100");
                JOptionPane.showMessageDialog(null,"Enter Valid Account No");
            }
        }
        if(e.getSource()==enq)
        {
            int a1 = ac1.getText().length();
            if(a1 == 10)
            {
                try
                {
                    Class.forName("com.mysql.jdbc.Driver");
                    Connection conn =DriverManager.getConnection("jdbc:mysql://localhost:33060/atm","root","sagar");
                    String sql1 = "select cash from atm where account_no = ?";
                    PreparedStatement st = conn.prepareStatement(sql1);
                    st.setString(1,ac1.getText());
                    ResultSet rs1 = st.executeQuery();
                    while(rs1.next())
                    {
                        String i = rs1.getString(1); 
                        rs.setText(i + "  Rs");
                    }
                    rs1.close();
                    st.close();
                }
                catch(ClassNotFoundException | SQLException ex1)
                {
                    System.out.println("sql Error");
                }
            }
            else
            {
                JOptionPane.showMessageDialog(null,"Enter Valid Account No");
            }
        }
        if(e.getSource()== con)
        {
            int a1 = pe.getText().length();
            int a2 = pie.getText().length();
            if(a1 == 10 && a2 == 4)
            {
                try
                {
                    Class.forName("com.mysql.jdbc.Driver");
                    Connection conn =DriverManager.getConnection("jdbc:mysql://localhost:33060/atm","root","sagar");
                    String sql = "update atm set pin = ? where account_no = ?";
                    PreparedStatement pstmt = conn.prepareStatement(sql);
                    pstmt.setString(1,pie.getText());
                    pstmt.setString(2,pe.getText());
                    JOptionPane.showMessageDialog(this,"Pin Changed Successfully");
                    pstmt.executeUpdate();
                    pstmt.close();
                }
                catch(ClassNotFoundException | SQLException | HeadlessException ae)
                {
                    System.out.println(ae);
                }
            }
            else
            {
                String msg = "ENTER VALID ACCOUNT NO / PIN SHOULD BE OF ONLY 4 DIGITS";
                String title = "ERROR"; 
                int type = JOptionPane.ERROR_MESSAGE;
                JOptionPane.showMessageDialog(null,msg,title,type);
            }
        }
        if(e.getSource()== confirm)
        {
            int a1 = t.getText().length();
            if(a1 == 10)
            {
                Random pin = new Random();
                int res = pin.nextInt(10000-1000);
                String res1 = String.valueOf(res);
                l2.setText(res1);
            }
            else
            {
                String msg = "ENTER VALID ACCOUNT NO";
                String title = "ERROR"; 
                int type = JOptionPane.ERROR_MESSAGE;
                JOptionPane.showMessageDialog(null,msg,title,type);
            }
        }
        if(e.getSource()== ok)
        {
            int t = Integer.parseInt(tf1.getText());
            int to = Integer.parseInt(tf3.getText());
            int top = Integer.parseInt(tf4.getText());
            int topi = Integer.parseInt(tf5.getText());
            int a1 = t*2000+to*500+top*200+topi*100;
            String a11 = String.valueOf(a1);
            int a = tca.getText().length();
            if(a == 10)
            try
            {
                Class.forName("com.mysql.jdbc.Driver");
                Connection conn = DriverManager.getConnection("jdbc:mysql://localhost:33060/atm","root","sagar");
                String sql1 = "update atm set cash = cash - ? where account_no = ?";
                PreparedStatement pstmt = conn.prepareStatement(sql1);
                pstmt.setString(1,a11);
                pstmt.setString(2,tca.getText());
                JOptionPane.showMessageDialog(this , "Take your Cash " + a11 + " Rs");
                pstmt.executeUpdate();
                pstmt.close(); 
            }
            catch(ClassNotFoundException | SQLException | HeadlessException ae)
            {
                System.out.println(ae);
            }
            else
            {
                JOptionPane.showMessageDialog(this, "Enter Valid Account No");
            }
        }
    }
public static void main(String[]args)
{
        new atm();
}
}
