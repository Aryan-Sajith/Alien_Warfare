import express, {Application, Request, Response} from "express"

// Server setup
const app: Application = express();
const PORT = 3000;

// Basic middleware
app.use(express.json());

// Basic test route
app.get("/", (req: Request, res: Response) => {
    res.send("Server is running!");
});

// Start the server
app.listen(PORT, () => {
    console.log(`Server is running at port: ${PORT}`);
})

