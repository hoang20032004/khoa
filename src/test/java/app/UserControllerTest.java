package app;

import org.junit.jupiter.api.*;
import static org.junit.jupiter.api.Assertions.*;

public class UserControllerTest {
    private UserController controller;

    @BeforeEach
    void setUp() {
        controller = new UserController();
        controller.registerUser("test", "1234");
    }

    @Test 
    void testRegisterSuccess() {
        assertTrue(controller.registerUser("new", "pass"));
    }

    @Test
    void testRegisterExisting() {
        assertFalse(controller.registerUser("test", "1234"));
    }

    @Test
    void testLoginSuccess() {
        assertTrue(controller.loginUser("test", "1234"));
    }

    @Test
    void testLoginWrongPassword() {
        assertFalse(controller.loginUser("test", "0000"));
    }
}
