package breakout;

import java.io.IOException;
import javax.swing.JFrame;

public final class Screen extends JFrame{
    
    public Screen(Settings settings, KeyEvents ke) throws IOException{
        add(settings.canvas);
        addKeyListener(ke);
        setSize(settings.screenWidth, settings.screenHeight);
        setTitle("BreakOut - Java");
        setVisible(true);
        setResizable(false);
        setLocationRelativeTo(null);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    }
}
