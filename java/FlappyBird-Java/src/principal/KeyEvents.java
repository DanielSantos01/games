package principal;

import java.awt.event.KeyEvent;
import java.awt.event.KeyListener;

public class KeyEvents implements KeyListener{
    private final Settings settings;
    private final Bird bird;
    
    public KeyEvents(Settings set, Bird brd){
        settings = set;
        bird = brd;
    }

    @Override
    public void keyTyped(KeyEvent ke) {}

    
    @Override
    public void keyPressed(KeyEvent ke) {
        switch(ke.getKeyCode()){
                case KeyEvent.VK_SPACE:
                    if((settings.preStart || settings.start)){
                        
                        settings.preStart = false;
                        settings.start = true;
                        
                        if(bird.rect.y >= 10  && !(settings.touchPipe)) settings.fall = settings.birdUpValue;
                        else settings.fall = 0;
                        
                    }else{
                        bird.centerBird();
                        settings.preStart = true;
                        settings.gameOver = false;
                        if(settings.touchPipe) settings.touchPipe = false;
                    }
                    
                    break;
                
                default: break;
        }            
    }

    
    @Override
    public void keyReleased(KeyEvent ke) {}
    
}
