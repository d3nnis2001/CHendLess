package com.chendless;

import org.springframework.beans.factory.InitializingBean;
import org.springframework.stereotype.Service;

@Service
public class InitializeDatabase implements InitializingBean {

    /**
    @Autowired
    public InitializeDatabase() {
    }
     **/

    @Override
    public void afterPropertiesSet() {
    }
}
