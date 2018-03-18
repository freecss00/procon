vector<edge> g[N];
bool used[N];

void add_edge(int u, int v, int c){
    g[u].push_back((edge){v, c, (int)g[v].size()});
    g[v].push_back((edge){u, 0, (int)g[u].size() - 1});
}

// Send maximum amount of flow along the found path.
int dfs(int v, int t, int f){
    if(v == t) return f;
    used[v] = true;
    rep(i,g[v].size()){
        edge &e = g[v][i];
        if(!used[e.to] and e.cap > 0){
            int d = dfs(e.to, t, min(f, e.cap));
            if(d > 0){
                e.cap -= d;
                g[e.to][e.rev].cap += d;
                return d;
            }
        }
    }
    return 0;
}

// As long as there is a path from the source to the sink,
// with available capacity on all edges in the path,
// send flow along one of the paths.
int max_flow(int s, int t){
    int flow = 0;
    while(1){
        memset(used, 0, sizeof(used));
        int f = dfs(s, t, INF);
        if(f == 0) return flow;
        flow += f;
    }
}
