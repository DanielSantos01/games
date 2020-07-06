package breakout;

import java.awt.event.KeyEvent;
import java.awt.event.KeyListener;

public class KeyEvents implements KeyListener{
    private final Settings settings;
    private final Bar bar;
    
    public KeyEvents(Settings config, Bar ba){
        settings = config;
        bar = ba;
    }

    @Override
    public void keyTyped(KeyEvent ke) {
    }

    @Override
    public void keyPressed(KeyEvent ke) {
        switch(ke.getKeyCode()){
            case KeyEvent.VK_RIGHT:
                if(bar.x <= settings.screenWidth - bar.width){
                    bar.x += 4;
                }
                break;
            case KeyEvent.VK_LEFT:
                 if(bar.x > 0){
                    bar.x -= 4;
                }
                break;
        }
    }

    @Override
    public void keyReleased(KeyEvent ke) {
        
    }
    
}
