package breakout;

import java.awt.event.KeyEvent;
import java.awt.event.KeyListener;

public class KeyEvents implements KeyListener{
    
    private final Settings settings;
    private final Bar bar;
    private final Ball ball;
    
    public KeyEvents(Settings config, Bar ba, Ball bal){
        settings = config;
        bar = ba;
        ball = bal;
    }

    @Override
    public void keyTyped(KeyEvent ke) {
    }

    @Override
    public void keyPressed(KeyEvent ke) {
        
        switch(ke.getKeyCode()){
            
            case KeyEvent.VK_RIGHT:
                
                if(bar.x < settings.screenWidth - bar.width){
                    bar.x += bar.moveValue;
                    if(settings.preStart) ball.x += bar.moveValue;
                }
                break;
                
            case KeyEvent.VK_LEFT:
                
                 if(bar.x > 0){
                    bar.x -= bar.moveValue;
                    if (settings.preStart) ball.x -= bar.moveValue;   
                }
                break;
                
            case KeyEvent.VK_SPACE:
                
                if(settings.preStart){
                    settings.preStart = false;
                    settings.start = true;
                }
            
            default:
                break;
        }
    }

    @Override
    public void keyReleased(KeyEvent ke) {
        
    }
    
}
