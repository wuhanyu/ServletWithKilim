package com.wuhanyu.kilim;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;

import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import java.io.IOException;
import java.io.PrintWriter;

@Controller
@RequestMapping("/sync")
public class SyncController extends HttpServlet {
    public static Logger log = LoggerFactory.getLogger(SyncController.class);

    @RequestMapping(method = RequestMethod.GET)
    public void doGet(HttpServletRequest req, HttpServletResponse response) throws ServletException, IOException {
        try {
            Thread.sleep(3000);
        } catch (InterruptedException e) {
            log.error("io error", e);
        }
    }

    public void doPost(HttpServletRequest req, HttpServletResponse resp) throws javax.servlet.ServletException, java.io.IOException {
        doGet(req,resp);
    }
}
