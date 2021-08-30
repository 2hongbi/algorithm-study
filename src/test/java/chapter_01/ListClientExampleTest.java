package chapter_01;

import org.junit.Test;

import java.util.ArrayList;
import java.util.List;

import static org.hamcrest.core.IsInstanceOf.instanceOf;
import static org.junit.Assert.*;

public class ListClientExampleTest {

    /*
        Test method for {@link ListClientExample}
     */
    @Test
    public void getList() {
        ListClientExample lce = new ListClientExample();
        List list = lce.getList();
        assertThat(list, instanceOf(ArrayList.class) );
    }
}