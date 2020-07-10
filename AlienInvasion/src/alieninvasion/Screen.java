package alieninvasion;

import java.awt.Color;
import java.awt.Graphics2D;
import java.awt.event.KeyEvent;
import java.awt.event.KeyListener;
import javax.swing.JFrame;

public class Screen extends JFrame{
    private final Settings settings;
    private final Color color;
    
    public Screen(Settings set, KeyListener ke){
        settings = set;
        color = new Color(230, 230, 230);
        add(settings.canvas);
        addKeyListener(ke);
        setTitle("Alien Invasion");
        setSize(settings.screenWidth, settings.screenHeight);
        setResizable(false);
        setLocationRelativeTo(null);
        setDefaultCloseOperation(EXIT_ON_CLOSE);
        setVisible(true);
    }
    
    protected void fill(Graphics2D g){
        g.setColor(color);
        g.fillRect(0, 0, settings.screenWidth, settings.screenHeight);
    }
}
