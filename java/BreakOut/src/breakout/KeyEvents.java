package breakout;

import java.awt.event.KeyEvent;
import java.awt.event.KeyListener;

public class KeyEvents implements KeyListener{
    private final Settings settings;
    private final Bar bar;
    private final Ball ball;
    private final int moveConst;
    public KeyEvents(Settings config, Bar ba, Ball bal){
        settings = config;
        bar = ba;
        ball = bal;
        moveConst = 5;
    }

    @Override
    public void keyTyped(KeyEvent ke) {
    }

    @Override
    public void keyPressed(KeyEvent ke) {
        
        switch(ke.getKeyCode()){
            
            case KeyEvent.VK_RIGHT:
                
                if(bar.x < settings.screenWidth - bar.width){
                    bar.x += moveConst;
                    if(settings.preStart){
                        ball.x += moveConst;
                    }
                }
                break;
                
            case KeyEvent.VK_LEFT:
                
                 if(bar.x > 0){
                    bar.x -= moveConst;
                    if (settings.preStart){
                        ball.x -= moveConst;
                    }
                }
                break;
        }
    }

    @Override
    public void keyReleased(KeyEvent ke) {
        
    }
    
}
