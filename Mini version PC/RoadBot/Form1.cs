using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.Threading;
using System.Threading.Tasks;
using AForge;
using AForge.Video;
using AForge.Video.DirectShow;
using System.Net.Sockets;
using System.Net;

namespace RoadBot
{
    public partial class Form1 : Form
    {
        FilterInfoCollection CaptureDevice;
        VideoCaptureDevice FinalFrame;

        String host = "10.0.0.14", serv = "10.0.0.19";
        string send = "", take = "";
        bool send_bool = false, take_bool = false;
        int x1 = 0, x2 = 0, y1 = 0, y2 = 0;

        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            host = textBox1.Text;
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            Task task = new Task(Task);
            Task task2 = new Task(Server);
            task2.Start();
            task.Start();
            textBox1.Text = host;
            label1.Text = host;
        }

        void Task()
        {
            CaptureDevice = new FilterInfoCollection(FilterCategory.VideoInputDevice);
            FinalFrame = new VideoCaptureDevice();
            MJPEGStream video = new MJPEGStream("http://" + host + ":8080/?action=stream"); //http://192.168.1.36
            video.NewFrame += new NewFrameEventHandler(FinalFrame_NewFrame);
            video.Start();
        }

        void Server()
        {
            const int port = 9090; // порт для прослушивания подключений
            IPAddress localAddr = IPAddress.Parse(serv);
            TcpListener server = new TcpListener(localAddr, port);
            server.Start();

            while (true)
            {
                TcpClient client = server.AcceptTcpClient();
                NetworkStream stream = client.GetStream();
                byte[] data = new byte[256];
                int bytes = stream.Read(data, 0, data.Length); // получаем количество считанных байтов
                take = Encoding.UTF8.GetString(data, 0, bytes);
                byte[] data1 = Encoding.UTF8.GetBytes(send);
                stream.Write(data1, 0, data1.Length);
                client.Close();
            }
        }

        void FinalFrame_NewFrame(object sender, NewFrameEventArgs eventArgs)
        {
            Bitmap bmp = (Bitmap)eventArgs.Frame.Clone();
            pictureBox1.Image = bmp;
            GC.Collect();
        }

        private void pictureBox1_MouseClick(object sender, MouseEventArgs e)
        {
            Bitmap bmp = (Bitmap)pictureBox1.Image;
        }
    }
}