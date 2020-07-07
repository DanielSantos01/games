package breakout;

import java.awt.Color;
import java.awt.Graphics2D;
import java.io.IOException;
import javax.swing.JFrame;

public final class Screen extends JFrame{
    Settings settings;
    public Screen(Settings set, KeyEvents ke) throws IOException{
        settings = set;
        add(set.canvas);
        addKeyListener(ke);
        setSize(settings.screenWidth, settings.screenHeight);
        setTitle("BreakOut - Java");
        setVisible(true);
        setResizable(false);
        setLocationRelativeTo(null);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    }
    
    public void fillBackground(Graphics2D g){
        g.setColor(Color.black);
        g.fillRect(0, 0, settings.screenWidth, settings.screenHeight);
    }
}
