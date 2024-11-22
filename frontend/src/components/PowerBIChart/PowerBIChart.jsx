import React from "react";
import { PowerBIEmbed } from "powerbi-client-react";
import { models } from "powerbi-client";
import './PowerBIChart.css';

const PowerBIChart = () => {
    return (
            <PowerBIEmbed
                embedConfig={{
                type: "report",
                embedUrl:
                "https://app.powerbi.com/view?r=eyJrIjoiY2RkNTJkZWUtMDQ3Ni00ZTBkLTg0ZGQtZWY5MjJjNTVmYjgxIiwidCI6ImNmNzJlMmJkLTdhMmItNDc4My1iZGViLTM5ZDU3YjA3Zjc2ZiIsImMiOjR9",
                accessToken: "",
                tokenType: models.TokenType.None,
                settings: {
                panes: {
                filters: {visible: false},
                pageNavigation: {visible: false},
            },
                layoutType: models.LayoutType.FitToPage,
                background: models.BackgroundType.Transparent,
            },
            }}
            cssClassName="powerbi-frame"
            frameBorder={0}
        />
    );
};

export default PowerBIChart;