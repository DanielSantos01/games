package breakout;

import java.awt.event.KeyEvent;
import java.awt.event.KeyListener;

public class KeyEvents implements KeyListener{
    
    private final Settings settings;
    private final Bar bar;
    private final Ball ball;
    private final Status score;
    
    public KeyEvents(Settings config, Bar ba, Ball bal, Status scor){
        settings = config;
        bar = ba;
        ball = bal;
        score = scor;
    }

    @Override
    public void keyTyped(KeyEvent ke) {
    }

    @Override
    public void keyPressed(KeyEvent ke) {
        
        switch(ke.getKeyCode()){
            
            case KeyEvent.VK_RIGHT:
                if(bar.rect.x < (settings.screenWidth - bar.rect.width)){
                    bar.rect.x += bar.moveValue;
                    if(settings.preStart) ball.rect.x += bar.moveValue;
                }
                break;
                
            case KeyEvent.VK_LEFT:
                 if(bar.rect.x > 0){
                    bar.rect.x -= bar.moveValue;
                    if (settings.preStart) ball.rect.x -= bar.moveValue;   
                }
                break;
                
            case KeyEvent.VK_SPACE:
                if(settings.preStart){
                    settings.preStart = false;
                    settings.start = true;
                }else if(settings.gameOver){
                    settings.gameOver = false;
                    settings.preStart = true;
                }
                break;
            
            default:
                break;
        }
    }

    @Override
    public void keyReleased(KeyEvent ke) {
        
    }
    
}
